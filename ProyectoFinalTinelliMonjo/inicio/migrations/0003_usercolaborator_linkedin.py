from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inicio", "0002_category_created_category_updated_perfil_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usercolaborator",
            name="linkedin",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
