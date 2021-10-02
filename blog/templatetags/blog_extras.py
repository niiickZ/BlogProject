from django import template
from ..models import Post, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.inclusion_tag('blog/inclusions/_archives.html')
def showArchives():
    return {'date_list': Post.objects.dates('created_time', 'month', order='DESC')}

@register.inclusion_tag('blog/inclusions/_tag_cloud.html')
def showTags():
    # tag_list = Tag.objects.all().order_by('name')
    tag_list = Tag.objects.annotate(num=Count('post'))  # 统计tag对应的文章数量并存储在num里
    return {'tag_list': tag_list}