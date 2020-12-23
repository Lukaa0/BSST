# Generated by Django 3.0.3 on 2020-03-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0017_auto_20200303_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodationpage',
            old_name='tour_price',
            new_name='tour_content_change_warning',
        ),
        migrations.AddField(
            model_name='accommodationpage',
            name='administration_charge',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='accommodationpage',
            name='flat_fees',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='accommodationpage',
            name='per_person_charges',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='accommodationpage',
            name='administration_fee',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='accommodationpage',
            name='breakfast_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='accommodationpage',
            name='community_fund',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
