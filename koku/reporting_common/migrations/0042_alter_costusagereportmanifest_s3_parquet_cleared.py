# Generated by Django 4.2.11 on 2024-06-28 12:00
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("reporting_common", "0041_diskcapacity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="costusagereportmanifest",
            name="s3_parquet_cleared",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
