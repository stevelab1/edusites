# Generated by Django 3.1.3 on 2020-12-12 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20201212_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='file',
        ),
    ]
