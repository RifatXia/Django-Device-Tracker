# Generated by Django 4.0.5 on 2023-09-01 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_remove_laptop_brand_remove_mobile_brand_device_brand_and_more'),
        ('company', '0004_remove_employee_devices'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('condition_on_checkout', models.CharField(blank=True, max_length=1000)),
                ('condition_on_return', models.CharField(blank=True, max_length=1000)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.employee')),
            ],
        ),
    ]
