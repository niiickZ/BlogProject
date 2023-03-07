from django.shortcuts import render
from .models import Diary
import markdown

# Create your views here.

def showDiary(request):
    diary_list = Diary.objects.all().order_by('-time')

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.nl2br',
    ])

    for diary in diary_list:
        diary.content = md.convert(diary.content)

    return render(request, 'diary/diary.html', {'diary_list': diary_list})
