# Generated by Django 2.2.24 on 2022-01-07 19:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0028_auto_20220107_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
