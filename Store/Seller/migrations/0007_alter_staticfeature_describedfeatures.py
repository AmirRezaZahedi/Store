# Generated by Django 4.2.5 on 2023-10-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0006_alter_staticfeature_describedfeatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticfeature',
            name='describedFeatures',
            field=models.ManyToManyField(to='Seller.staticfeature'),
        ),
    ]