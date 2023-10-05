# Generated by Django 4.2.4 on 2023-10-05 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0002_alter_category_referencecategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staticfeature',
            name='category',
        ),
        migrations.AddField(
            model_name='staticfeature',
            name='category',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to='Seller.category'),
            preserve_default=b'I01\n',
        ),
    ]