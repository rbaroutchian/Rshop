# Generated by Django 5.1 on 2024-12-29 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0017_user_address_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
