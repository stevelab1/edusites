# Generated by Django 3.1.3 on 2020-12-14 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_auto_20201214_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.subject'),
            preserve_default=False,
        ),
    ]
