# Generated by Django 4.2.4 on 2024-02-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0002_alter_seller_store_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seller",
            name="store_name",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]