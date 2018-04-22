from django.urls import path, include
from . import upload, play, comment

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')), django自带的用户表单
    path('upload/', upload.upload_view, name='upload'),
    path('play_file_obj/<slug:series>/<slug:name>/', play.play_file_obj, name='play_file_obj'),
    path('play_ajax_obj/<slug:series>/<slug:name>/', play.play_ajax_obj, name='play_ajax_obj'),
    path('play/<slug:series>/', play.play_view, name='play'),
    path('play/', play.play_index_view, name='play_index'),
    path('comment/post_comment/', comment.post_comment_view, name='post_comment'),
    path('comment/', comment.render_comment_view, name='comment'),

]
