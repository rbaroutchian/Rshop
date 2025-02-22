import random

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    about_user = models.TextField(max_length=500, null=True, blank=True, verbose_name='درباره من')
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل کاربر')
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    address_org = models.TextField(null=True, blank=True, verbose_name='آدرس اصلی')
    address2 = models.TextField(null=True, blank=True, verbose_name='آدرس دوم')
    address3 = models.TextField(null=True, blank=True, verbose_name='آدرس سوم')
    address4 = models.TextField(null=True, blank=True, verbose_name='آدرس چهارم')
    address5 = models.TextField(null=True, blank=True, verbose_name='آدرس پنجم')
    address6 = models.TextField(null=True, blank=True, verbose_name='آدرس ششم')
    avatar = models.ImageField(upload_to='media/profile', null=True, blank=True, verbose_name='تصویر ')

    class Meta:
        verbose_name='کاربر'
        verbose_name_plural='کاربران'


    def __str__(self):
        return self.get_full_name()

    def generate_verification_code(self):
        self.verification_code = str(random.randint(100000, 999999))
        self.save()
