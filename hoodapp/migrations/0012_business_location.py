# Generated by Django 2.2.24 on 2022-01-04 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0011_auto_20220104_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.Location'),
        ),
    ]
