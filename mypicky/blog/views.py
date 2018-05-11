from django.shortcuts import render, get_object_or_404
from . models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list_view(request):
    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 3)
    page = request.GET.get('page', 1)
    try:
        posts = Paginator.page(page)
    except PageNotAnInteger:
        posts = Paginator.page(1)
    except EmptyPage:
        posts = Paginator.page(paginator.num_pages)

    return render(request, 'posts/list.html', {'posts': posts})


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'posts/detail.html', {'post': post})