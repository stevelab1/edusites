# Generated by Django 3.1.3 on 2020-11-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20201114_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/users/2020/11/14/6dedf44d3ea322809634744be06e4447--abandoned-castles-abandone_omca0a', upload_to='users/%Y/%m/%d/'),
        ),
    ]