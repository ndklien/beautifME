# Generated by Django 3.1.1 on 2020-12-11 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201210_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 11, 12, 42, 47, 308138)),
        ),
    ]
