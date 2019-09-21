from django.shortcuts import render, get_object_or_404
from .forms import ArticleForm
from .models import Article

# Create your views here.


def create_article_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()

    context = {
        'form': form
    }

    return render(request, "blogs/article_create.html", context)


def get_article_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        'object': obj
    }

    return render(request, "blogs/article_detail.html", context)


def get_all_articles_view(request):
    object_list = Article.objects.all()

    context = {
        'object_list': object_list
    }

    return render(request, "blogs/article_list.html", context)
