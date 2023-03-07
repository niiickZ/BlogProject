from django.db import models
from django.utils import timezone

# Create your models here.

class Diary(models.Model):
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
