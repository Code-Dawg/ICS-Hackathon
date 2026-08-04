"""
==============================================================================
BLOG MODELS
Educational Articles, Categories, & Digital Safety Guides.
==============================================================================
"""

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    summary = models.TextField()
    content = models.TextField()
    read_time = models.CharField(max_length=20, default="5 min read")
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
