# Generated by Django 2.2.8 on 2019-12-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0010_auto_20191203_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='headings_font_color',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='headings_font_family',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='headings_font_size',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='paragraphs_font_color',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='paragraphs_font_family',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='paragraphs_font_size',
            field=models.CharField(max_length=600, null=True),
        ),
    ]