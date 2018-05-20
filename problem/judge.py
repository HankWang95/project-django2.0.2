from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import ProblemForm, CodeForm
from .models import Problem
import os
import subprocess

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_dir')

def problem_list(request):
    problem_list = Problem.objects.all()
    '''listt = []
    for obj in problem_list:
        if obj.series not in list:
            list.append(obj.series)'''
    return render(request, 'problem/problem_list.html', {'list':problem_list})

def problem_show(request, id):
    problem = Problem.objects.get(id = id) 
    return render(request, 'problem/problem_show.html', {'problem':problem})

def judge_pass(request):
    return HttpResponse(u'评判通过') 

def judge_unpass(request):
    return HttpResponse(u'评判未通过') 

def judge_compileError(request):
    return HttpResponse(u'编译错误')

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
            #number = str(form.cleaned_data['number'])
            language_dict = {
                'C': 'c',
                'C++': 'cpp',
                'JAVA': 'java',
                'Python': 'py'}                
            language = 'test.'+language_dict.get(language_choice)

            #DIR = os.path.join(CODE_DIR, number)
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
            #result = os.popen(command).read()
            p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
            out, err = p.communicate()
            result = str(out)
            os.unlink(filename)
            #with open('result', 'w+') as f:
                #f.write(result)
            if 'false' in result:
                return redirect(reverse(judge_compileError))
            else:
                if 'WRONG_ANSWER' in result:
                    return redirect(reverse(judge_unpass))
                elif '"TIME_LIMIT_EXCEEDED"' in result:
                    return redirect(reverse(judge_timeExceeded))
                elif '"MEMORY_LIMIT_EXCEEDED"' in result:
                    return redirect(reverse(judge_memoryExceeded))
                else:
                    return redirect(reverse(judge_pass))
        else:
            return render(request, 'problem/commit.html', {'form': form})
        return redirect('code_judge')
    else:
        form = CodeForm()
        return render(request, 'problem/commit.html', {'form': form})
