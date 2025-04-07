from django.shortcuts import get_object_or_404, render

from .models import Category, Post

from django.utils import timezone


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    for post in post_list:
        post.category_slug = post.category.slug
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, slug):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ),
        slug=slug
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, pk):
    template = 'blog/category.html'
    category = get_object_or_404(Category, id=pk)
    if not category.is_published:
        return render(request, '404.html', status=404)
    post = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'post': post,
    }
    return render(request, template, context)
