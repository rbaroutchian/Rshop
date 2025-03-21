from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='admin_dashboard'),
    path('articles/', views.ArticleListView.as_view(), name='admin_articles'),
    path('articles/comments', views.ArticleCommentAdmin.as_view(), name='admin_articles_comment'),
    path('articles/category', views.ArticleCategoryAdmin.as_view(), name='admin_articles_category'),
    path('add-articles/', views.ArticleAdd.as_view(), name='admin_add_articles'),
    path('add-comment/', views.CommentAdd.as_view(), name='admin_add_comment_articles'),
    path('articles/edit/<pk>', views.ArticleUpdateView.as_view(), name='admin_edit_article'),
    path('articles/comment/edit/<pk>', views.CommentUpdateView.as_view(), name='admin_edit_comment_article'),
    path('articles/cat/edit/<pk>', views.ArticleCatUpdateView.as_view(), name='admin_edit_cat_article'),
    path('articles/delete/<int:pk>/', views.ArticleDelete.as_view(), name='admin_delete_article'),
    path('articles/comment/delete/<int:pk>/', views.CommentDelete.as_view(), name='admin_delete_comment_article'),
    path('users/', views.UserListView.as_view(), name='admin_users'),
    path('users/delete/<int:pk>/', views.UserDelete.as_view(), name='admin_users_delete'),
    path('users/add/', views.UserAdd.as_view(), name='admin_users_add'),
    path('users/edit/<pk>', views.UserUpdateView.as_view(), name='admin_edit_users'),

]
