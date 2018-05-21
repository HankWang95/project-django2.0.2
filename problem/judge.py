#coding:utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import ProblemForm, CodeForm
from .models import Problem
import os
import json

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_dir')


# 题目列表
def problem_list(request,series):
    problem_list = Problem.objects.all().filter(series=series)
    add = False
    user = request.user
    if problem_list[0].owner == user:
        add = True
    '''listt = []
    for obj in problem_list:
        if obj.series not in list:
            list.append(obj.series)'''
    return render(request, 'problem/problem_list.html', {'list':problem_list,
                                                         'add': add,
                                                         'series': series})


# 题目信息展示
def problem_show(request, id):
    problem = Problem.objects.get(id=id)
    add = False
    if problem.owner == request.user:
        add = True
    return render(request, 'problem/problem_show.html', {'problem':problem, 'add': add})


def judge_pass(request):
    return HttpResponse(u'评判通过') 


def judge_unpass(request):
    return HttpResponse(u'评判未通过') 


def judge_timeExceeded(request):
    return HttpResponse(u'超时')


def judge_memoryExceeded(request):
    return HttpResponse(u'内存限制')


def code_judge(request, id):
    if request.method == 'POST':

        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            language_choice  = form.cleaned_data['lang_choice']
            language_dict = {
                'C': 'c',
                'C++': 'cpp',
                'JAVA': 'java',
                'Python': 'py'}                
            language = 'test.'+language_dict.get(language_choice)

            DIR = os.path.join(CODE_DIR, str(id))
            count = 0
            for fn in os.listdir(DIR):
                count += 1
            count //=2
            filename = os.path.join(DIR, language)
            with open(filename, 'w+') as f:
                f.write(code)

            command = 'ljudge --user-code '+filename
            i = 1
            while(i <= count):
                inputcase = os.path.join(DIR, (str(i)+'.in'))
                outputcase = os.path.join(DIR, (str(i)+'.out'))
                command = command + ' --testcase --input '+inputcase+' --output '+outputcase
                i += 1
            #command = 'ljudge --user-code test.cpp --testcase --input 1.in --output 1.out --testcase --input 2.in --output 2.out' 
            jsonresult = os.popen(command).read()
            result = json.loads(jsonresult)
            with open('result','w+') as f:
                f.write(str(result))
            os.unlink(filename)
            if not result['compilation']['success']:
                compile_error = result['compilation']['log'].splitlines()
                return render(request, 'problem/compileError.html', {'list':compile_error})

            for i in result['testcases']:
                if 'WRONG_ANSWER' in i['result']:
                    return redirect(reverse(judge_unpass))
            for i in result['testcases']:
                if 'TIME_LIMIT_EXCEEDED' in i['result']:
                    return redirect(reverse(judge_timeExceeded))
                if 'MEMORY_LIMIT_EXCEEDED' in i['result']:
                    return redirect(reverse(judge_memoryExceeded))
            return redirect(reverse(judge_pass))
        else:
            return render(request, 'problem/commit.html', {'form': form})
    else:
        form = CodeForm()
        return render(request, 'problem/commit.html', {'form': form, 'id':id})
