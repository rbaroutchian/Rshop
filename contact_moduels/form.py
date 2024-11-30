from django import forms
from .models import Contact

class ContactForm(forms.Form):
    fullname = forms.CharField(
        label='نام و نام خانوادگی:',
        max_length=50,
        error_messages={
        'riquired':'نام و نام خانوادگیحتم باید وارد شود',
        'max_lenght':'طول کاراکتر نام و نام خانوادگی بادی حداکثر 50 باشد'
        },
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
        )
    email = forms.EmailField(
        label='ایمیل:',
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder': 'ایمیل شما'
        })

                             )
    phone = forms.CharField(
        label='تلفن همراه:',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'تلفن همراه'
        })
    )
    Title = forms.CharField(
        label='موضوع:',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'موضوع پیام'

        })
    )
    message = forms.CharField(
        label='پیام خود را بنویسید:',
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder': 'پیام خود را بنویسید',
            'rows':'6',
            'id':'cf-message'
        })
    )

class ContactModelForm(forms.ModelForm):
    class Meta:
       model=Contact
       fields=['Fullname', 'Email', 'Title', 'Phone', 'Message']
       widgets={
           'Fullname':forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'نام و نام خانوادگی',
            }),
           'Email':forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder': 'ایمیل شما',
            }),
           'Title': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'موضوع پیام شما',
           }),
           'Phone': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'موبایل شما',
           }),
           'Message': forms.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'پیام شما',
               'rows': '6',
               'id': 'cf-message'

           })

       }
       labels={
           'Fullname':'نام و نام خانوادگی',
           'Email':'ایمیل',
           'Title':'موضوع',
           'Phone':'تلفن همراه',
           'Message':'پیام خود را بنویسید'


       }
       error_messages={
           'fullname':{
               'required':'لطفا نام و نام خانوادگی را وارد کنید'

           }
       }
       # fields='__all__'

class ProfileImage(forms.Form):
    url_image = forms.ImageField()
