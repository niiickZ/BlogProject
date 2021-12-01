from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('tag/<int:pk>/', views.tags, name='tag'),
    path('category/<int:pk>/', views.categories, name='category'),
    path('search/', views.search, name='search')
]