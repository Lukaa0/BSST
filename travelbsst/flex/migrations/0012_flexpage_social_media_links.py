# Generated by Django 2.2.6 on 2019-12-13 03:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0011_auto_20191203_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='social_media_links',
            field=wagtail.core.fields.StreamField([('SocialMedia', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.TextBlock(required=True)), ('social_media_url', wagtail.core.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
    ]
