# Generated by Django 4.2.5 on 2023-10-11 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='referenceCategory',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, related_name='child_categories', to='Seller.category'),
        ),
    ]
