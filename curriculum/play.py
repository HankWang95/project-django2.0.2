from django.shortcuts import render
from django.http import FileResponse
from .models import CurriculumInfo
import os

# 暂时的测试播放文件夹，迁移时要注意更改
PLAY_PATH = '/Users/wanghc/Desktop/dev-2.0/mysite/curriculum/upload_dir'


# 渲染播放界面，series = 文件夹名称（系列名）
def play_view(request, series):
    q_list = CurriculumInfo.objects.all().filter(series=series)
    path = []
    request.session['curriculum_series'] = series
    for obj in q_list:
        path.append(os.path.join(obj.series,obj.file_name))

    return render(request, 'curriculum/play.html', {'path':path,})


# 视频的播放导航（按系列）
def play_index_view(request):
    q_list = CurriculumInfo.objects.all()
    list = []
    for obj in q_list:
        if obj.series not in list:
            list.append(obj.series)
    return render(request, 'curriculum/play_index.html',{'list':list})



# AJAX对象，用来返回一个播放器对象，具体的视频文件需要继续调用其他url
# 参数：name：用来生成一个src（视频源url），传给play_file_obj（src）
def play_ajax_obj(request, series, name):
    return render(request, 'curriculum/play_ajax_obj.html', {
        'series': series, 'name':name,
    })

# 用来返回一个文件对象，用来填充视频内容
def play_file_obj(request, series, name):
    src = os.path.join(PLAY_PATH, os.path.join(series, name))+'.mp4'

    response = FileResponse(open(src, 'rb'), content_type='video/mp4')
    return response
