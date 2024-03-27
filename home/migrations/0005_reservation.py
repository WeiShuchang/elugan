# Generated by Django 5.0.3 on 2024-03-27 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_driver'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestor_name', models.CharField(max_length=100)),
                ('office_department_college', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('appointment_status', models.CharField(max_length=50)),
                ('requestor_address', models.CharField(blank=True, max_length=100)),
                ('number_of_passengers', models.IntegerField()),
                ('destination', models.CharField(max_length=50)),
                ('date_of_travel', models.DateField(blank=True, null=True)),
                ('purpose_of_travel', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]