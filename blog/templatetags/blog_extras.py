from django import template
from ..models import Post, Tag, Category, FriendLink
from django.db.models.aggregates import Count

register = template.Library()

@register.inclusion_tag('blog/inclusions/_archives.html')
def showArchives():
    return {'date_list': Post.objects.dates('created_time', 'month', order='DESC')}

@register.inclusion_tag('blog/inclusions/_category.html')
def showCategories():
    cate_list = Category.objects.annotate(num=Count('post'))
    return {'cate_list': cate_list}

@register.inclusion_tag('blog/inclusions/_tag_cloud.html')
def showTags():
    # tag_list = Tag.objects.all().order_by('name')
    tag_list = Tag.objects.annotate(num=Count('post'))  # 统计tag对应的文章数量并存储在num里
    return {'tag_list': tag_list}

@register.inclusion_tag('blog/inclusions/_friends_link.html')
def showFriendlinks():
    link_list = FriendLink.objects.all()
    return {'link_list': link_list}