from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inicio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Fecha de edición"
            ),
        ),
        migrations.AddField(
            model_name="perfil",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AddField(
            model_name="perfil",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Fecha de edición"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Fecha de edición"
            ),
        ),
        migrations.AddField(
            model_name="postusercolaborator",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AddField(
            model_name="postusercolaborator",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Fecha de edición"
            ),
        ),
        migrations.AddField(
            model_name="suscripcion",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AddField(
            model_name="suscripcion",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Fecha de edición"
            ),
        ),
        migrations.AddField(
            model_name="usercolaborator",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AddField(
            model_name="usercolaborator",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Fecha de edición"
            ),
        ),
    ]
