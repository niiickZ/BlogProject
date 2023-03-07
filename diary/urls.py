from django.urls import path, include
from . import views

app_name = 'diary'
urlpatterns = [
    path('niki', views.showDiary, name='index'),
]