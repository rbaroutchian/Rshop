from django.urls import path
from . import views

urlpatterns = [
    path('userdashboard', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('address-page', views.AddressEditPage.as_view(), name='edit_address_page'),
    path('user-basket', views.user_basket, name='user-basket'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail'),
    path('change-order-detail', views.change_order_details_count, name='change_order_details_count'),

]
