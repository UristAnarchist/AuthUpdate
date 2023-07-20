# Generated by Django 4.2.3 on 2023-07-20 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0006_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 22, 27, 8, 990701)),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]