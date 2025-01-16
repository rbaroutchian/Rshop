from django import forms
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'mobile', 'email', 'address_org',
                  'address2', 'address3', 'address4',
                  'address5', 'address6', 'about_user']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'address_org': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'address2': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'address3': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'address4': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'address5': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'address6': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),

            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'id': 'message'
            })
        }

        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'mobile': 'موبایل',
            'address_org': 'آدرس اصلی',
            'address2': 'آدرس دوم',
            'address3': 'آدرس سوم',
            'address4': 'آدرس چهارم',
            'address5': 'آدرس پنجم',
            'address6': 'آدرس ششم',
            'about_user': 'درباره شخص',
        }
