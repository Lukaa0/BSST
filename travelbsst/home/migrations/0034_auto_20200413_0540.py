# Generated by Django 3.0.3 on 2020-04-13 05:40

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20200413_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='boooking_request_subtitle',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='boooking_request_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='community_describtion_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='community_name_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='email_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='emails',
            field=wagtail.core.fields.StreamField([('emails', wagtail.core.blocks.StructBlock([('country', wagtail.core.blocks.TextBlock(required=True)), ('email', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='finishing_text',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='fullname_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organisation_address_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organisation_booking_contact_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organisation_email_address_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organisation_language_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organisation_name_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organisation_phone_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organisation_website_placeholder',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organistaion_culture_describtion_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organistaion_describtion_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organistaion_protect_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='organistaion_support_describtion_title',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='select_email_text',
            field=models.CharField(max_length=1600, null=True),
        ),
    ]
