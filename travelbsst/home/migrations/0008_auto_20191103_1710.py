# Generated by Django 2.2.6 on 2019-11-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191103_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='section_with_video_additional_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_with_video_short_text',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
