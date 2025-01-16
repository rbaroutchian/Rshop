from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse
from unidecode import unidecode

from account_module.models import User


# Create your models here.

class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True, blank=True, related_name='parentcategories')
    Ctitle = models.CharField(max_length=300, db_index=True, verbose_name="عنوان")
    urltitle = models.CharField(max_length=300, db_index=True, verbose_name="عنوان در url" )
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف / حذف نشده')

    def __str__(self):
        return self.Ctitle

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural= 'دسته بندی ها'

class ProductBrand(models.Model):
    title = models.CharField(max_length=300,verbose_name='نام برند', db_index=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name='برند'
        verbose_name_plural= 'برند ها'


    def __str__(self):
        return self.title



# class ProductInfo(models.Model):
#     color = models.CharField(max_length=300, verbose_name='رنگ')
#     size = models.CharField(max_length=300, verbose_name='سایز')
#
#     def __str__(self):
#         return f'{self.color} - {self.size}'
#
#     class Meta:
#         verbose_name='اطلاعات تکمیلی'
#         verbose_name_plural= 'تمامی اطلاعات تکمیلی'

class ProductTag(models.Model):
    Caption = models.CharField(max_length=200, verbose_name='عنوان تگ')

    class Meta:
        verbose_name ='کپشن'
        verbose_name_plural= 'مدیریت کپشن ها'

    def __str__(self):
        return self.Caption
class Product(models.Model):

    Ptitle = models.CharField(max_length=300, db_index=True, verbose_name='عنوان محصول')
    # Pinfo = models.OneToOneField(ProductInfo, on_delete=models.CASCADE, null=True,
    #                              related_name='product_info',
    #                              verbose_name='اطلاعات تکمیلی',)
    Pcategory = models.ManyToManyField(ProductCategory, blank=True, related_name='products', verbose_name='دسته بندی')
    product_tag = models.ManyToManyField(ProductTag, verbose_name='تگ های محصول')
    #protect برای محافظت کردن می باشد
    #casade برای این است که اگر اون دسته بندی پاک شد همه محصولات آن پاک می شود
    ProductBrand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, verbose_name='برند محصول')
    Pprice = models.IntegerField(default=0, db_index=True, verbose_name='قیمت')
    short_description = models.CharField(max_length=360, null=True, db_index=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات محصول', null=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف / حذف نشده')
    Pimage = models.ImageField(default='media/aks/01.jpg', verbose_name='تصویر')
    slug = models.SlugField(default="", blank=True, db_index=True) #editable=False
    #دی بی ایندکس برای پرهیز از کندی سرعت می باشد

    #برای اینکه وقتی ادرس را کاربر وارد کرد همون آی دی که مربوط به این محصول هست ریورس کند
    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Ptitle, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.Ptitle} {self.Pprice}'

    class Meta:
        verbose_name='محصول'
        verbose_name_plural= 'محصولات'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    parent = models.ForeignKey('ProductComment', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='parentcomment', verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام و نم خانوادگی')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصول'


