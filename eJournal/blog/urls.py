from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from blog.models import Post

urlpatterns = [
url(r'^$', ListView.as_view(queryset = Post.objects.all(), template_name = "blog/post_list.html")),
#url(r'^$', views.post_list, name = 'post_list'),
url(r'^post/new/$', views.post_new, name = 'post_new'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
