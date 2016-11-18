from django.conf.urls import url
from blog.views import PostListView#, PostDetailView


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    #url(r'(?P<pk>[\w-]+)/$',
    #    PostDetailView.as_view(), name='post_detail'),
]
