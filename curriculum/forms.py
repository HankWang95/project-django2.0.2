from django import forms
from django.forms import ModelForm
from .models import Comment



class UploadForm(forms.Form):
    grade = forms.CharField(label='年级')
    series = forms.CharField(label='系列')
    number = forms.IntegerField(label='该视频为第几集')
    file = forms.FileField(label='请上传文件')



# 评论表单
class PostCommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea,max_length=140,label="输入留言内容")


