from django.views import generic
from .models import Post
from django.shortcuts import render

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post-list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def about(request):
    context = {}
    return render(request, 'about.html', context)


def packages(request):
    context = {}
    return render(request, 'packages.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def index(request):
    context = {}
    return render(request, 'index.html', context)


def one_package(request):
    context = {}
    return render(request, 'one_package.html', context)


def two_package(request):
    context = {}
    return render(request, 'two_package.html', context)


def three_package(request):
    context = {}
    return render(request, 'three_package.html', context)
