# Generated by Django 2.2.6 on 2019-11-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0002_auto_20191115_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutuspage',
            old_name='banner_title',
            new_name='banner_title_letter1',
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='banner_title_text',
            field=models.CharField(max_length=1600, null=True),
        ),
    ]
