from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View
from utils.email_service import send_email

from .models import User
from django.utils.crypto import get_random_string
from .form import RegisterForm, RegisterModelForm, LoginForm, ForgotPasswordForm, ResetPasswordForm

# Create your views here.
class AccountView(CreateView):
    form_class = RegisterModelForm
    template_name = 'account_module/register_page.html'
    success_url = reverse_lazy('login_page')


class Register(View):
    def get(self, request):
        register_form = RegisterModelForm()
        context={
            'register_form':register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterModelForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            # user : User = User.objects.filter(email__iexact=user_email).exists()
            user_exists = User.objects.filter(email__iexact=user_email).exists()
            if user_exists:
                register_form.add_error('email', 'ایمیل وارد  شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email
                )

                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری', new_user.email,
                           {'user': new_user},
                           'emails/active_account.html')
                return redirect(reverse('login_page'))


        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/login_page.html', context)

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('Email')
            user_pass = login_form.cleaned_data.get('Password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('Email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.acheck_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse_lazy('home'))
                    else:
                        login_form.add_error('Email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('Email', 'کاربری با مشخصات وارد شده یافت نشد')
        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login_page.html', context)

class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
            else:
                pass

        raise Http404


class ForgetPassword(View):
    def get(self, request: HttpRequest):
        forget_pass_form= ForgotPasswordForm(request.POST)
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('Email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user},
                           'emails/forgot_password.html')
                return redirect(reverse('home'))
                # return redirect(reverse('reset_password_page'))
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account_module/forgot_password.html', context)


class ResetPassword(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))

        reset_pass_form = ResetPasswordForm()

        context = {'reset_pass_form': reset_pass_form,
                   'user': user
                   }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_pass = reset_pass_form.cleaned_data.get('Password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))
        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'account_module/reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
