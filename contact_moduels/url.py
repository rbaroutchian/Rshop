from django.urls import path
from . import views

urlpatterns = [
    path('contactlist', views.contact, name='contact_page'),

]