# Generated by Django 2.2.6 on 2019-11-11 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_auto_20191111_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexpage',
            name='banner_image',
        ),
    ]