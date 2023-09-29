# Generated by Django 4.2.5 on 2023-09-29 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("spend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RevenueStatistic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                (
                    "revenue",
                    models.DecimalField(decimal_places=2, default=0, max_digits=9),
                ),
                (
                    "spend",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="spend.spendstatistic",
                    ),
                ),
            ],
        ),
    ]
