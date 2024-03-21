# Generated by Django 5.0.3 on 2024-03-20 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0007_remove_order_ht_products_alter_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_ht',
            name='image',
            field=models.ImageField(default=0, upload_to='products/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 10, 14, 54, 882944, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 10, 14, 54, 882944, tzinfo=datetime.timezone.utc)),
        ),
    ]