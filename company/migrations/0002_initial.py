# Generated by Django 4.0.5 on 2023-09-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='devices',
            field=models.ManyToManyField(to='device.device'),
        ),
    ]
