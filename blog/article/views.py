from django.shortcuts import render
from article.models import Article
# Create your views here.

def articles(request):
    return render(request, 'articles.html', {"articles":Article.objects.all()})


def article(request, article_id=1):
    return render(request, 'article.html', {'article': Article.objects.get(id=article_id)})