# Generated by Django 5.0.6 on 2024-07-10 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_translate_email_en_translate_hotline_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translate',
            name='email_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='hotline_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='our_location_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='title_en',
        ),
    ]
