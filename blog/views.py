"""
==============================================================================
BLOG VIEWS
Article list and detail views.
==============================================================================
"""

from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def article_list_view(request):
    """Article catalog listing."""
    articles = Article.objects.select_related('category').all()
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'articles': articles, 'categories': categories})

def article_detail_view(request, slug):
    """Single article reader."""
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/detail.html', {'article': article})
