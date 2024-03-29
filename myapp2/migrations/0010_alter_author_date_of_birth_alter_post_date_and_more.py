# Generated by Django 5.0.3 on 2024-03-20 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0009_shooter_alter_author_date_of_birth_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 16, 51, 42, 711412, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 16, 51, 42, 712409, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='shooter',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
