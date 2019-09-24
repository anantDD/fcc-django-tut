from django.shortcuts import render, get_object_or_404
from .forms import ArticleForm
from .models import Article

from django.views.generic import (
    ListView,
    DetailView,
)

# Create your views here.


class ArticleListView(ListView):
    template_name = "blogs/article_list1.html"
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    # queryset = Article.objects.filter(id=2)
    # print(queryset)

    def get_object(self):
        print(self.kwargs)
        print('therse')
        _id = self.kwargs.get("id")
        return get_object_or_404(Article, id=_id)


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

    return render(request, "blogs/article_list1.html", context)
