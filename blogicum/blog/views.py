from django.shortcuts import get_object_or_404, render

from .models import Category, Post

from datetime import timezone


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.values(
    ).filter(is_published=True,
             category__is_published=True
             ).order_by('-pub_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.values(
        ).filter(is_published=True,
                 pub_date__lte=timezone.now()
                 ),
        id=id
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, pk):
    template = 'blog/category.html'
    category = get_object_or_404(Category, pk=pk)
    post = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=False
    )
    context = {
        'post': post,
        'category': category
    }
    return render(request, template, context)
