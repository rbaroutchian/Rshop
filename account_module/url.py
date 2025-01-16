from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('forget-pass/', views.ForgetPassword.as_view(), name='forget_password_page'),
    path('reset-pass/<str:active_code>', views.ResetPassword.as_view(), name='reset_password_page'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),

    path('verify-code/', views.VerifyCodeView.as_view(), name='verify_code_page')
    # path('resend-code/', views.ResendCodeView.as_view(), name='resend_code_page'),
]

