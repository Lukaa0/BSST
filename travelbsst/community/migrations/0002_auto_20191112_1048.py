# Generated by Django 2.2.6 on 2019-11-12 10:48

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitypage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='communitypage',
            name='accommodation_cards',
            field=wagtail.core.fields.StreamField([('accommodationcards', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('accommodation_name', wagtail.core.blocks.TextBlock(required=True)), ('accommodation_price', wagtail.core.blocks.TextBlock(required=True)), ('attribute1_title', wagtail.core.blocks.TextBlock(required=True)), ('attribute1_text', wagtail.core.blocks.TextBlock(required=True)), ('attribute2_title', wagtail.core.blocks.TextBlock(required=True)), ('attribute2_text', wagtail.core.blocks.TextBlock(required=True)), ('attribute3_title', wagtail.core.blocks.TextBlock(required=True)), ('attribute3_text', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='accommodation_section_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='activities_cards_title',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='activity_cards',
            field=wagtail.core.fields.StreamField([('activitycard', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.TextBlock(required=True)), ('l1', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='additional_activities_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='additional_activity_cards',
            field=wagtail.core.fields.StreamField([('additionalactivitycard', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('activity_description', wagtail.core.blocks.TextBlock(required=True)), ('availability', wagtail.core.blocks.TextBlock(required=True)), ('group_size', wagtail.core.blocks.TextBlock(required=True)), ('price_per_person', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='community_description',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='community_name',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='images',
            field=wagtail.core.fields.StreamField([('images', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='images_section_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='meet_the_community_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='meet_the_community_title_subtitle',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='communitypage',
            name='members_cards',
            field=wagtail.core.fields.StreamField([('memberscards', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.core.blocks.TextBlock(required=True)), ('surname', wagtail.core.blocks.TextBlock(required=True)), ('person_info', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
    ]