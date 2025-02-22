from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='admin_dashboard'),
    path('articles/', views.ArticleListView.as_view(), name='admin_dashboard'),
    path('articles/edit/<pk>', views.ArticleUpdateView.as_view(), name='admin_edit_article'),
]
