# Generated by Django 5.1 on 2024-09-16 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_itenscompra"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
