from django.contrib import admin
from .models import Diary

class DiaryAdmin(admin.ModelAdmin):
    list_display = ['time']

# Register your models here.
admin.site.register(Diary, DiaryAdmin)
