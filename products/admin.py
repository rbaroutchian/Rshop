from django.contrib import admin
from . import models

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['Ptitle']
    }
    list_display = ['__str__', 'Pprice', 'is_active']
    list_filter = ['Pcategory', 'ProductBrand', 'Pprice']
    list_editable = ['is_active', 'Pprice']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)



