# Generated by Django 3.1.3 on 2020-11-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/hmklz8dtf/image/upload/v1/media/users/2020/11/14/3abc6275419f468bf41a10b64a90f31b--st-etienne-cathedrals_jqbogy', upload_to='users/%Y/%m/%d/'),
        ),
    ]
