# Generated by Django 2.2.6 on 2019-11-11 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20191111_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='additional_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_image2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_image3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='content',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='main_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='video_image',
        ),
    ]