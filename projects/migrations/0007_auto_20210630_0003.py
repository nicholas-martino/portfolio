# Generated by Django 3.1.2 on 2021-06-30 00:03

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210629_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=markdownfield.models.MarkdownField(rendered_field='text_rendered'),
        ),
    ]
