# Generated by Django 4.2.15 on 2024-11-01 12:49
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0064_delete_dataexportrequest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exchangerates",
            name="currency_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("aud", "AUD"),
                    ("brl", "BRL"),
                    ("cad", "CAD"),
                    ("chf", "CHF"),
                    ("cny", "CNY"),
                    ("dkk", "DKK"),
                    ("eur", "EUR"),
                    ("gbp", "GBP"),
                    ("hkd", "HKD"),
                    ("inr", "INR"),
                    ("jpy", "JPY"),
                    ("nok", "NOK"),
                    ("nzd", "NZD"),
                    ("sek", "SEK"),
                    ("sgd", "SGD"),
                    ("usd", "USD"),
                    ("zar", "ZAR"),
                ],
                max_length=5,
            ),
        ),
    ]