# Generated by Django 2.2.6 on 2019-12-13 03:00

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_homepage_main_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='social_media_icon',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='social_media_links',
            field=wagtail.core.fields.StreamField([('SocialMedia', wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('social_media_url', wagtail.core.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
    ]
