# Generated by Django 2.2.6 on 2019-11-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20191111_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image1_colored_text_line1',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image1_colored_text_line2',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image1_text_line1',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image1_text_line2',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image2_colored_text_line1',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image2_colored_text_line2',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image2_text_line1',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image2_text_line2',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image3_colored_text_line1',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image3_colored_text_line2',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image3_text_line1',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image3_text_line2',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
