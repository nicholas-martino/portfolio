# Generated by Django 3.1.2 on 2021-07-08 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0019_auto_20210708_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
