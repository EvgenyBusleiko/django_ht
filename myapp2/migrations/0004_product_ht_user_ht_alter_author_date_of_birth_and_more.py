# Generated by Django 5.0.3 on 2024-03-10 12:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0003_author_biography_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_ht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(max_length=8)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_ht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 10, 12, 28, 55, 722270, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 10, 12, 28, 55, 722270, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Order_ht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(to='myapp2.product_ht')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.user_ht')),
            ],
        ),
    ]