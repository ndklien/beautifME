# Generated by Django 3.1.1 on 2020-11-17 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_merge_20201117_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 11, 17, 15, 24, 45, 770862)),
        ),
    ]
