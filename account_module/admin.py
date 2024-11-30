from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

admin.site.register(models.User, UserAdmin)
