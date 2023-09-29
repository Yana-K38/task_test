# Generated by Django 4.2.5 on 2023-09-29 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spend", "0001_initial"),
        ("revenue", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="revenuestatistic",
            name="spend",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="revenue",
                to="spend.spendstatistic",
            ),
        ),
    ]
