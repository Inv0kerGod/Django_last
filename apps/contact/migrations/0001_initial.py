# Generated by Django 5.0.6 on 2024-07-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Translate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Заголовок баннера"),
                ),
                (
                    "hotline",
                    models.CharField(max_length=255, verbose_name="Горячая линия"),
                ),
                (
                    "our_location",
                    models.CharField(max_length=255, verbose_name="Локация"),
                ),
                (
                    "email",
                    models.CharField(max_length=255, verbose_name="Официальная почта"),
                ),
            ],
            options={
                "verbose_name": "",
                "verbose_name_plural": "Перевод страницы контакты",
            },
        ),
    ]
