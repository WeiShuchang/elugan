# Generated by Django 5.0.3 on 2024-03-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_picture',
            field=models.ImageField(blank=True, default='cars/default-img.jpg', null=True, upload_to='drivers/'),
        ),
    ]
