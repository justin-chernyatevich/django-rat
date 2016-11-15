from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^$', RedirectView.as_view(permanent=True,
        url=reverse_lazy('blog:blog_list')), name='home'),
]
