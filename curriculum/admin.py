from django.contrib import admin
from curriculum.models import CurriculumInfo
from .move import move_video_passed
# Register your models here.

admin.site.register(CurriculumInfo)
