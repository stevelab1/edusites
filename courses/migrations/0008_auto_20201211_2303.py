# Generated by Django 3.1.3 on 2020-12-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20201211_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['updated']},
        ),
    ]