# Generated by Django 5.0.3 on 2024-03-12 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0006_alter_author_date_of_birth_alter_post_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_ht',
            name='products',
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 13, 48, 39, 100434, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order_ht',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 13, 48, 39, 100434, tzinfo=datetime.timezone.utc)),
        ),
    ]
