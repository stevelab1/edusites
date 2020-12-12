# Generated by Django 3.1.3 on 2020-12-12 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20201212_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]