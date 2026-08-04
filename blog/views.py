"""
==============================================================================
BLOG VIEWS
Article list and detail views.
==============================================================================
"""

from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from journey.views import LEVELS_METADATA

def article_list_view(request):
    """Learning chapter catalog, followed by optional supporting articles."""
    articles = Article.objects.select_related('category').all()
    categories = Category.objects.all()
    chapters = [
        {
            'number': level['level'],
            'title': level['title'],
            'description': level['desc'],
            'icon': level['icon'],
        }
        for level in LEVELS_METADATA
    ]
    return render(request, 'blog/index.html', {
        'articles': articles,
        'categories': categories,
        'chapters': chapters,
    })

def article_detail_view(request, slug):
    """Single article reader."""
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/detail.html', {'article': article})
