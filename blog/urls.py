from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('search/', views.search, name='search')
]