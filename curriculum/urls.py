from django.urls import path
from . import upload, play, comment, my_series, all_series

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')), django自带的用户表单

    path('my/series_list/', my_series.my_series_list_view, name='my_series_list'),
    path('my/series/<int:series>', my_series.my_series_view, name='my_series'),
    path('join/series/<int:series>', my_series.join_series_view, name='join_series'),
    path('mine/', my_series.mine_view, name='mine'),


    path('all_series/', all_series.show_all_series_view, name='all_series'),
    path('show_series/<int:series>', all_series.show_series_view, name='show_series'),
    path('search/series/<int:kind>', all_series.show_series_view, name='search_series_for_kind'),

    path('series/add/', upload.add_series_view, name='add_series'),
    path('my/series/<int:series>/add/curriculum/', upload.add_curriculum_view, name='add_curriculum'),


    path('play_file_obj/<int:id>/', play.play_file_obj, name='play_file_obj'),
    path('play_ajax_obj/<int:id>/', play.play_ajax_obj, name='play_ajax_obj'),
    path('play/<int:series>/', play.play_view, name='play'),
    # path('play/', play.play_index_view, name='play_index'),
    path('play/<int:series>/post_comment/', comment.post_comment_view, name='post_comment'),
    # path('play/<int:series>/comment/', comment.render_comment_view, name='comment'),
    # path('move_video_passed/', move.move_video_passed, name='move_video_passed'),
    # path('move_video_unpassed/', move.move_video_unpassed, name='move_video_unpassed'),
]
