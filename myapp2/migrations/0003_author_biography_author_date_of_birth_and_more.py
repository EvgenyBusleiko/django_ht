# Generated by Django 5.0.3 on 2024-03-07 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_author_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(default=1234),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 18, 43, 52, 394996, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='author',
            name='lastname',
            field=models.CharField(default='1234', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 18, 43, 52, 394996, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
