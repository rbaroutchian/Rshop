# Generated by Django 5.1 on 2024-12-25 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_articlecomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentarticlecategory', to='blog.articlecategory', verbose_name='دسته بندی والد'),
        ),
    ]
