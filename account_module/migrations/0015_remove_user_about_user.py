# Generated by Django 5.1 on 2024-12-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0014_remove_user_address_remove_user_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='about_user',
        ),
    ]
