from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import strip_tags
from django.urls import reverse
import markdown
from mdx_math import MathExtension

class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)

class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)

class Post(models.Model):
    def __str__(self):
        return self.title

    def addViews(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            MathExtension(enable_dollar_delimiter=True)
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:110]

        super().save(*args, **kwargs)

    def getAbsoluteURL(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)


