# Generated by Django 3.1.2 on 2021-07-05 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0009_auto_20210705_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 5, 19, 8, 28, 300024)),
        ),
    ]
