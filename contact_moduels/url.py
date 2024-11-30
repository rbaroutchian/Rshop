from django.urls import path
from . import views

urlpatterns = [
    # path('contactlist', views.contact, name='contact_page'),
    path('', views.contactView.as_view(), name="contact_page"),
    path('profile', views.Createuser.as_view(), name="profile"),
    path('profile_user', views.ProfileUser.as_view(), name="profile_page")

]