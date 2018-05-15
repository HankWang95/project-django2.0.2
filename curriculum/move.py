from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import CurriculumInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
import datetime
import os
import shutil

VIDEO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'video_dir')
PASSED_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passed_dir')
UNPASSED_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unpassed_dir')

def move_video_passed(srcfile):
    name = srcfile[srcfile.rfind('/')+1:]
    dstfile = os.path.join(PASSED_DIR, name)
    if not os.path.exists(PASSED_DIR):
        os.makedirs(PASSED_DIR)
    shutil.move(srcfile, dstfile)

def move_video_unpassed(srcfile):
    name = srcfile[srcfile.rfind('/')+1:]
    dstfile = os.path.join(UNPASSED_DIR, name)
    if not os.path.exists(UNPASSED_DIR):
        os.makedirs(UNPASSED_DIR)
    shutil.move(srcfile, dstfile)

@permission_required('curriculum.move_video',login_url='/')
def move_video_passed(request):
    if request.method == 'GET':
        move_video_passed(request.GET.get('name'))

def move_video_unpassed(request):
    if request.method == 'GET':
        move_video_unpassed(request.GET.get('name'))