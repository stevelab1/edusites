# Generated by Django 3.1.2 on 2020-11-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodboard', '0003_image_total_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
