# Generated by Django 2.2.6 on 2019-12-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20191203_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='additional_text',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headings_font_color',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headings_font_family',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headings_font_size',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image1_colored_text_line1',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image1_colored_text_line2',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image1_text_line1',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image1_text_line2',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image2_colored_text_line1',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image2_colored_text_line2',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image2_text_line1',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image2_text_line2',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image3_colored_text_line1',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image3_colored_text_line2',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image3_text_line1',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image3_text_line2',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='main_text',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='paragraphs_font_color',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='paragraphs_font_family',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='paragraphs_font_size',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='partners_section_title',
            field=models.CharField(max_length=1600, null=True),
        ),
    ]