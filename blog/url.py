from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.ArticleListView.as_view(), name='article_list'),
    path('artcat/<str:category>', views.ArticleListView.as_view(), name='article_by_category'),
    path('<int:id>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/add-article-comment/', views.add_article_comment, name='add_article_comment')


]

