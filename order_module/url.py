from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order/', views.add_product_to_order, name='add_product_to_order'),
    path('request_payment/', views.request_payment, name='request_payment'),
    path('verify_payment/', views.verify_payment, name='verify_payment'),
]
