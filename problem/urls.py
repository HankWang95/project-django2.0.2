from django.urls import path, include
from . import judge, add, case

# Create your views here.

urlpatterns = [

    path('code/commit/<int:id>', judge.code_judge, name='code_commit'),
    path('add_problem/', add.problem_add, name='add_problem'),
    path('add_case/<int:id>', case.case_add, name='add_case'),
    path('judge_pass/', judge.judge_pass, name='judge_pass'),
    path('judge_unpass/', judge.judge_unpass, name='judge_unpass'),
    path('judge_compileError/', judge.judge_compileError, name='compile_error'),
    path('judge_timeExceeded/', judge.judge_timeExceeded, name='time_exceeded'),
    path('judge_memoryExceeded/', judge.judge_timeExceeded, name='memory_exceeded'),
    path('problem_list/', judge.problem_list, name='problem_list'),
    path('problem_show/<int:id>', judge.problem_show, name='problem_show'),
]
