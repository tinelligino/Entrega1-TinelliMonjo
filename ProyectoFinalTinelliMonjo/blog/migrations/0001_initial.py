# Generated by Django 4.1.1 on 2022-11-07 04:53

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("profile_picture", models.ImageField(upload_to="")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=20)),
                ("subtitle", models.CharField(max_length=20)),
                ("slug", models.SlugField()),
                ("thumbnail", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Perfil",
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
                ("name", models.CharField(max_length=50)),
                ("createdate", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "User Colaborator Perfils",
            },
        ),
        migrations.CreateModel(
            name="Suscripcion",
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
                ("name", models.CharField(max_length=50)),
                ("createdate", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "User Colaborator Suscripcions",
            },
        ),
        migrations.CreateModel(
            name="UserColaborator",
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
                ("email", models.EmailField(max_length=200)),
                ("description", models.TextField()),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="avatar"),
                ),
                ("createdate", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "perfil",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.perfil",
                    ),
                ),
                (
                    "suscripcion",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.suscripcion",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "User colaborators",
            },
        ),
        migrations.CreateModel(
            name="PostUserColaborator",
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
                ("title", models.CharField(max_length=100)),
                ("content", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("createdate", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "User Post colaborators",
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField()),
                ("overview", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField()),
                ("thumbnail", models.ImageField(upload_to="")),
                ("featured", models.BooleanField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.author"
                    ),
                ),
                ("categories", models.ManyToManyField(to="blog.category")),
            ],
        ),
    ]