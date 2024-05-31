# Generated by Django 5.0.6 on 2024-05-31 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_remove_customer_nid_passport_image_and_more'),
        ('hotel_owner', '0003_room'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.IntegerField()),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('booking_status', models.CharField(choices=[('Not Confirmed', 'Not Confirmed'), ('Confirmed', 'Confirmed')], default='Not Confirmed', max_length=15)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=10)),
                ('special_request', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel_owner.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel_owner.room')),
            ],
        ),
    ]