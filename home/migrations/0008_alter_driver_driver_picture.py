# Generated by Django 5.0.3 on 2024-03-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_car_car_picture_alter_driver_driver_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_picture',
            field=models.ImageField(blank=True, default='drivers/default-driver.jpeg', null=True, upload_to='drivers/'),
        ),
    ]
