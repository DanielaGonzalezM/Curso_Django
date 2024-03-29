# Generated by Django 5.0.1 on 2024-01-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portafolio", "0002_alter_project_options_remove_project_update_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="projects", verbose_name="Imagen"),
        ),
    ]
