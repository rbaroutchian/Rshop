from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

from .models import User


class RegisterForm(forms.Form):
    Email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        })
    )
    Phone_number = forms.CharField(
        label='موبایل',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موبایل'
        })
    )
    Password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور'

        })
    )
    ConfirmPassword = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور'
        })
    )

    def clean_ConfirmPassword(self):
        password = self.cleaned_data('password')
        ConfirmPassword = self.cleaned_data('ConfirmPassword')

        if password == ConfirmPassword:
            return ConfirmPassword

        raise ValidationError('کلمه عبور و تکرار کلمه عبور یکسان نمی باشند')


class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': 'form-control',
        'placeholder': 'رمز عبور ',
        'autocomplete': 'new-password',
        'style': 'border: 1px solid #6a11cb; padding: 10px; font-size: 14px;'

    }), label="رمز عبور")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تأیید رمز عبور',
        'autocomplete': 'new-password',
        'style': 'border: 1px solid #2575fc; padding: 10px; font-size: 14px;'

    }), label="تأیید رمز عبور")

    class Meta:
        model = User
        fields = ('email', 'mobile', 'username', 'password', 'confirm_password')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
                'autocomplete': 'email',
                'style': 'border: 1px solid #00b894; padding: 10px; font-size: 14px;'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موبایل',
                'autocomplete': 'mobile',
                'style': 'border: 1px solid #00b894; padding: 10px; font-size: 14px;'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام کاربری',
                'autocomplete': 'username',
                'style': 'border: 1px solid #00b894; padding: 10px; font-size: 14px;'

            })

        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("رمز عبور و تأیید آن مطابقت ندارند.")


class LoginForm(forms.Form):
    Email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    Password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور'

        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class ForgotPasswordForm(forms.Form):
    Email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    Password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'کلمه عبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    ConfirmPassword = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار کلمه عبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
