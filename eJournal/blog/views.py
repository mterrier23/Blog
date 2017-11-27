from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
# next two are apart of a diff tutorial, it works without them
from .models import Post
from django.utils import timezone
# works without that line though?
from .forms import PostForm
# from itertools import chain
# from operator import attrgetter

def index(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
    # result_list = sorted(chain(object_list), key = attrgetter('created_at'))
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
