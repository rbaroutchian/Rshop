# Generated by Django 5.1 on 2025-02-02 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_articlecomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_set', to='blog.articlecomment', verbose_name='والد'),
        ),
    ]
