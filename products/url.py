from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('', views.index, name='home'),
    path('productlist', views.product_list, name='product_list'),
    path('<str:slug>', views.product_detail, name='detail'),

              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))