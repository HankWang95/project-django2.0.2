from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

# 自定义课程类型（树形结构）
class KindOfSeries(models.Model):
    parent_kind = models.ForeignKey('self', blank=True, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


# 系列模型
class Series(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Series_owner', default=User.objects.get(id=1).id)
    kind = models.ForeignKey(KindOfSeries, on_delete=models.CASCADE, related_name='Series_kind', verbose_name='所属类型')
    number_of_participants = models.IntegerField(default=0, verbose_name='参加课程人数')
    approval_status = models.BooleanField(default=False)
    introduce = models.CharField(max_length=200, blank=True, null=True, verbose_name='系列简介')


# 未审核&审核未通过 课程模型
class UnauditedCurriculum(models.Model):
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UnauditedCurriculum_editor', blank=True, null=True)
    created_time = models.DateTimeField(default=now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UnauditedCurriculum_owner')
    name = models.CharField(max_length=50, verbose_name='课程名')
    path = models.FilePathField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='UnauditedCurriculum_series')
    number = models.IntegerField(verbose_name='集数')
    attachment = models.FilePathField(blank=True, null=True, verbose_name='附件文件')
    approval_status = models.BooleanField(default=False)

    class Meta:
        # permissions 会在数据库创建属于该模块的一个自定义权限
        permissions = (
            ('upload_file', '可以上传文件'),
            ('move_video', '移动视频所在库'),
        )
        ordering = ['number']


# 审核通过课程
class Curriculum(models.Model):
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Curriculum_editor', blank=True,
                               null=True)
    created_time = models.DateTimeField(default=now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Curriculum_owner')
    file_name = models.CharField(max_length=50)
    path = models.FilePathField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='Curriculum_series')
    number = models.IntegerField(verbose_name='集数')
    attachment = models.FilePathField()


# 存储评论
class Comment(models.Model):
    body = models.TextField('正文', max_length=300)
    created_time = models.DateTimeField('创建时间', default=now)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE,related_name='Comment_series')
    parent_comment = models.ForeignKey('self', verbose_name="上级评论", blank=True, null=True, on_delete=models.CASCADE)
    is_enable = models.BooleanField('是否显示', default=True, blank=False, null=False)

    class Meta:
        ordering = ['-created_time']
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'

    def __str__(self):
        return self.body

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class CurriculumParticipation(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    curriculum = models.IntegerField(default=1)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)