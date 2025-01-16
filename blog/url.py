from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.ArticleListView.as_view(), name='article_list'),
    path('artcat/<str:category>', views.ArticleListView.as_view(), name='article_by_category'),
    path('<int:id>', views.ArticleDetailView.as_view(), name='article_detail'),

]

