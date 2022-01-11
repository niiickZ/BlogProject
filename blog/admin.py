from django.contrib import admin
from .models import Post, Tag, Category, FriendLink

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(FriendLink)
