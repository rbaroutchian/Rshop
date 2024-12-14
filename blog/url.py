from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.ArticleListView.as_view(), name='article_list')
]

