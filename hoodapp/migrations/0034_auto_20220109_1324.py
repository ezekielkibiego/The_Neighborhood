# Generated by Django 2.2.24 on 2022-01-09 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0033_auto_20220108_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_name',
            new_name='name',
        ),
    ]
