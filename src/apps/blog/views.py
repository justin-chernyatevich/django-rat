from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.views.generic import ListView
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def listing(request):
        contact_list = Contacts.objects.all()
        paginator = Paginator(contact_list, 8)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        return render_to_response('blog/post_detail.html', {"contacts":
                                                                contacts})