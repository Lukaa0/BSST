# Generated by Django 2.2.9 on 2020-02-02 07:27

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0014_auto_20200202_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodationpage',
            name='room_option_prices',
            field=wagtail.core.fields.StreamField([('RoomOptionPrices', wagtail.core.blocks.StructBlock([('price', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accommodationpage',
            name='room_options',
            field=wagtail.core.fields.StreamField([('RoomOptions', wagtail.core.blocks.StructBlock([('room_option', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
    ]
