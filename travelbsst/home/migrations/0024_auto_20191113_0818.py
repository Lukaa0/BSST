# Generated by Django 2.2.6 on 2019-11-13 08:18

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20191111_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='partners',
            field=wagtail.core.fields.StreamField([('partners', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('button_url', wagtail.core.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partners_section_title',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
