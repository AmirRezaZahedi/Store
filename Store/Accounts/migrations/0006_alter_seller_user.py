# Generated by Django 4.2.4 on 2023-08-29 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_seller_store_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='seller', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]