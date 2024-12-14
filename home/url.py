from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home')
    path('', views.homeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about_page')
]
