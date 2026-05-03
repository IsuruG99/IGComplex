from django.shortcuts import render

from .models import Article


def blog_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/blog.html', {'articles': articles})

