# Generated by Django 2.2.6 on 2019-11-07 07:20

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20191107_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('header_text', wagtail.core.blocks.TextBlock(help_text='text to the right', required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='text to the right', required=True)), ('additional_text', wagtail.core.blocks.TextBlock(help_text='text to the right', required=True))])), ('text_and_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('header_text', wagtail.core.blocks.TextBlock(help_text='text to the right', required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='text to the right', required=True)), ('additional_text', wagtail.core.blocks.TextBlock(help_text='text to the right', required=True))]))], blank=True, null=True),
        ),
    ]
