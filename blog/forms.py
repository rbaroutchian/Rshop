from django import forms
from .models import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شما'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن نظر'}),
        }
        labels = {
            'name': 'نام و نام خانوادگی',
            'email': 'ایمیل ',
            'text': 'نظر شما',
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')

        if not self.instance.user:
            if not name:
                raise forms.ValidationError("لطفاً نام خود را وارد کنید.")
            if not email:
                raise forms.ValidationError("لطفاً ایمیل خود را وارد کنید.")
        return cleaned_data
