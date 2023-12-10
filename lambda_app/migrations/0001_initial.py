# Generated by Django 5.0 on 2023-12-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aluno",
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
                ("nome", models.CharField(max_length=200)),
                ("cpf", models.CharField(max_length=11)),
                ("email", models.EmailField(max_length=200)),
                ("telefone", models.CharField(max_length=20)),
                ("matriculado", models.BooleanField(default=True)),
            ],
        ),
    ]