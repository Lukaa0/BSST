# Generated by Django 2.2.6 on 2019-11-07 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_homepage_partners_section_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='partners',
        ),
    ]