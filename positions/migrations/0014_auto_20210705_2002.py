# Generated by Django 3.1.2 on 2021-07-05 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0013_auto_20210705_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 5, 20, 2, 52, 149801)),
        ),
    ]
