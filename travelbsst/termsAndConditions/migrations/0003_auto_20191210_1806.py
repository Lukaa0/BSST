# Generated by Django 2.2.6 on 2019-12-10 18:06

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('termsAndConditions', '0002_termsandconditionpage_main_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='termsandconditionpage',
            name='general_text',
            field=wagtail.core.fields.RichTextField(default='default text 2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='termsandconditionpage',
            name='main_title',
            field=models.CharField(max_length=1600, null=True),
        ),
    ]