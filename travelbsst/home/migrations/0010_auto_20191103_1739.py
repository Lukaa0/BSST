# Generated by Django 2.2.6 on 2019-11-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191103_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='section_with_video_short_text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
