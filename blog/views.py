from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from pure_pagination import PaginationMixin

from .models import Post, Tag
import markdown
from mdx_math import MathExtension
import re

# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 1

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 增加文章阅读量
    post.addViews()

    # 文章主题markdown转html
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        MathExtension(enable_dollar_delimiter=True)
    ])
    post.body = md.convert(post.body)

    # 文章摘要
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})

def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def tags(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})