from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings


# Create your models here.


# 课程模型
# TODO：label：一个为上传文件加入的标签选项、用来搜索。最好用下拉菜单形式
class CurriculumInfo(models.Model):
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='curriculum_info')
    file_name = models.CharField(max_length=50)
    path = models.FilePathField()
    series = models.CharField(verbose_name='系列', max_length=50)
    price = models.IntegerField(verbose_name='价格')
    grade = models.CharField(verbose_name='年级', max_length=50)
    number = models.IntegerField(verbose_name='集数')

    class Meta:
        # permissions 会在数据库创建属于该模块的一个自定义权限
        permissions = (
            ('upload_file', '可以上传文件'),
            ('move_video', '移动视频所在库'),
        )


# 存储评论
class Comment(models.Model):
    body = models.TextField('正文', max_length=300)
    created_time = models.DateTimeField('创建时间', default=now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    curriculum = models.CharField(max_length=50)
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

