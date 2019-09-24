from django.urls import path

from .views import (
    get_all_articles_view,
    get_article_view,
    create_article_view,
    ArticleListView,
    ArticleDetailView
)

urlpatterns = [
    path('l', ArticleListView.as_view(), name='list'),
    path('', get_all_articles_view, name='list'),
    path('create/', create_article_view, name='create'),
    path('article/<int:id>', ArticleDetailView.as_view(), name='detail')
    # path('article/<int:id>', get_article_view, name='article-detail')
]
