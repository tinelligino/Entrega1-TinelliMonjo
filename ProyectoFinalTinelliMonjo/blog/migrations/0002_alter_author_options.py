# Generated by Django 4.1.1 on 2022-11-08 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={
                "verbose_name": "Autor",
                "verbose_name_plural": "Author [ Autor ]",
            },
        ),
    ]