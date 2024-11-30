from django.db import models

# Create your models here.
class Contact(models.Model):
    Title = models.CharField(max_length=300, verbose_name='عنوان پیام')
    Email = models.EmailField(max_length=300, verbose_name='ایمیل')
    Fullname = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    Phone = models.TextField(max_length=300, verbose_name='شماره تماس')
    Message = models.TextField(verbose_name='متن پیام مخاطب')
    admin_message = models.TextField(verbose_name='پاسخ ادمین', null=True, blank=True)
    is_read_admin = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد پیام')

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural= 'لیست تماس با ما'


class userProfile(models.Model):
    url_image = models.FileField(upload_to='media')

    # def __str__(self):
    #     return self.Title
    #
    # class Meta:
    #     verbose_name = 'تصویر دریافتی'
    #     verbose_name_plural = 'لیست تصویرهای دریافتی'
