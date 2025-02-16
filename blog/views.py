from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from pure_pagination import PaginationMixin
from django.contrib import messages
from django.db.models import Q

from .models import Post, Tag, Category
import markdown
from mdx_math import MathExtension
import re


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    ordering = ['-created_time']
    paginate_by = 10


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 增加文章阅读量
    post.addViews()

    # 文章主题markdown转html
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.nl2br',
        MathExtension(enable_dollar_delimiter=True)
    ])
    post.body = md.convert(post.body)

    # 文章目录
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Post.objects.filter(tags=t).order_by('-created_time')


class CategoryView(IndexView):
    def get_queryset(self):
        c = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=c).order_by('-created_time')


class ArchiveView(IndexView):
    def get_queryset(self):
        post_list = Post.objects.filter(
            created_time__year=self.kwargs['year'],
            created_time__month=self.kwargs['month']
        ).order_by('-created_time')
        return post_list


def search(request):
    q = request.GET.get('q')

    # 若查询为空则重定向至首页
    # if not q:
    #     messages.warning(request, '请输入搜索关键词')
    #     return redirect('blog:index')

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))

    # 若未查询到则提示并重定向至首页
    if post_list.count() == 0:
        messages.info(request, '未检索到相关文章')
        return redirect('blog:index')

    return render(request, 'blog/index.html', {'post_list': post_list})


# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})
#
# def archive(request, year, month):
#     post_list = Post.objects.filter(
#         created_time__year=year,
#         created_time__month=month
#     ).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})
#
# def categories(request, pk):
#     c = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=c).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})
#
# def tags(request, pk):
#     t = get_object_or_404(Tag, pk=pk)
#     post_list = Post.objects.filter(tags=t).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})