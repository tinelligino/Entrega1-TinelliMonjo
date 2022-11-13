# Generated by Django 4.1.1 on 2022-11-13 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("value", models.CharField(max_length=255)),
                (
                    "date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                ("user", models.CharField(max_length=50)),
                ("room", models.CharField(max_length=100)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Fecha de edición"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=100)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Fecha de edición"
                    ),
                ),
            ],
        ),
    ]
