# Generated by Django 4.2.4 on 2023-08-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_remove_customer_id_remove_seller_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='store_type',
            field=models.IntegerField(choices=[(0, 'لوازم خانگی'), (1, 'لبنیات'), (2, 'شیرینی فروشی'), (3, 'لوازم الکترونیک'), (4, 'سوپر مارکت')]),
        ),
    ]