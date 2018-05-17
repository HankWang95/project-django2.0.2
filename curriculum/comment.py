from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Comment
from .forms import PostCommentForm
from django.contrib.auth.decorators import login_required


# 发布评论
@login_required
def post_comment_view(request):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data['body']
            author = User.objects.get(username=request.user.username)
            curriculum = request.session['curriculum_series']
            post = Comment(body=body, author=author, curriculum=curriculum)
            post.save()
            url = '/play/'+curriculum
            return redirect(url)
        return redirect('/play/')



# 展示评论
def render_comment_view(request):
    list = []
    form = PostCommentForm()
    q = Comment.objects.filter(curriculum=request.session['curriculum_series'])
    for i in q:
        dict = {}
        dict['name'] = i.author.username
        dict['body'] = i.body
        dict['time'] = i.created_time
        dict['href'] = ""
        list.append(dict)
    return render(request, "curriculum/comment.html", {'form':form, 'list':list})