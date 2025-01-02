# Generated by Django 5.1.4 on 2025-01-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("username", models.CharField(max_length=50, verbose_name="username")),
                ("email", models.CharField(max_length=100, verbose_name="email")),
                ("password", models.CharField(max_length=50, verbose_name="password")),
            ],
        ),
    ]