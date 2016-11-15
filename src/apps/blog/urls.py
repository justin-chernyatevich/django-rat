from django.conf.urls import url
from blog.views import PostListView, PostDetailView

urlpatterns = [
    #url(r'^blog_list/$', PostListView.as_view(), name='post_list'),
    #url(r'^login/$', PostDetailView.as_view(), name='post_detail'),
]
