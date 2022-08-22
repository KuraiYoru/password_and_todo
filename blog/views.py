from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blogger

def trying(request):
    blogger = Blogger.objects.all()
    paginator = Paginator(blogger, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj': page_obj, 'blogger': blogger})


class BlogDetailView(DetailView): # новое
    model = Blogger
    template_name = 'blog/post_detail.html'

