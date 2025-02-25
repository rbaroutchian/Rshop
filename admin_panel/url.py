from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='admin_dashboard'),
    path('articles/', views.ArticleListView.as_view(), name='admin_articles'),
    path('add-articles/', views.ArticleAdd.as_view(), name='admin_add_articles'),
    path('articles/edit/<pk>', views.ArticleUpdateView.as_view(), name='admin_edit_article'),
    path('articles/delete/<int:pk>', views.ArticleDelete.as_view(), name='admin_delete_article'),
]
