from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    # path('productlist', views.product_list, name='product_list'),
    path('productlist', views.productListView.as_view(), name='product_list'),

    # path('<str:slug>', views.product_detail, name='detail'),
    path('<str:slug>', views.productDetailView.as_view(), name='detail'),
    # path('<int:pk>', views.productDetailView.as_view(), name='detail'),

               ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))