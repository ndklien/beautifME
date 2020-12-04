# Generated by Django 3.1.1 on 2020-12-04 04:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('product_size_in_ml', models.IntegerField(default=0)),
                ('product_img', models.ImageField(upload_to='product/images/')),
                ('price', models.IntegerField(default=0)),
                ('skintype', models.CharField(choices=[('DRY', 'Dry Skin'), ('OIL', 'Oliy Skin'), ('COMBI', 'Combination Skin'), ('NORM', 'Normal Skin'), ('ALL', 'All Skin Type')], max_length=5)),
                ('skin_cond', models.CharField(blank=True, choices=[('SEN', 'Sensitive Skin'), ('ACNE', 'Acne Skin'), ('AGE', 'Aging Skin')], max_length=5, null=True)),
                ('category', models.CharField(choices=[('MAKEUP_RM', 'Makeup Remover'), ('CLEANSE', 'Cleanser'), ('TONER', 'Toner'), ('SERUM', 'Serum'), ('MOIST', 'Moisturizer'), ('LOTION', 'Lotion'), ('MASK', 'Mask'), ('EYE', 'Eye Care'), ('SUN', 'Sun Care'), ('EXFOL', 'Exfoliators'), ('LIP', 'Lip Treatment')], max_length=10)),
                ('vote_down', models.IntegerField(default=0)),
                ('vote_up', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 12, 4, 11, 4, 17, 441591))),
                ('vote_down', models.IntegerField(default=0)),
                ('vote_up', models.IntegerField(default=0)),
                ('owner_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
