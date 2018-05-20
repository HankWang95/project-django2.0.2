from django.shortcuts import render, redirect
from .forms import ProblemForm
from .models import Problem

def problem_add(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            number = str(form.cleaned_data['number'])
            name = form.cleaned_data['name']
            tag = form.cleaned_data['tag']
            description = form.cleaned_data['description']
            input_description = form.cleaned_data['input_description']
            output_description = form.cleaned_data['output_description']
            input_sample = form.cleaned_data['input_sample']
            output_sample = form.cleaned_data['output_sample']
            time = str(form.cleaned_data['time'])
            memory = str(form.cleaned_data['memory'])
            new_problem = Problem(
                number = number,
                name = name,
                tag = tag,
                description = description,
                input_description = input_description,
                output_description = output_description,
                input_sample = input_sample,
                output_sample = output_sample,
                time = time,
                memory = memory)
            new_problem.save()
        else:
            return render(request, 'problem/problem.html', {'form': form})
        return redirect('add_problem')
    else:
        form = ProblemForm()
        return render(request, 'problem/problem.html', {'form': form})
