# Generated by Django 5.0.6 on 2024-05-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_owner', '0003_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='images',
            field=models.ImageField(upload_to='media/hotel_image/'),
        ),
        migrations.AlterField(
            model_name='hotelowner',
            name='address_proof',
            field=models.FileField(upload_to='media/address_proof/'),
        ),
        migrations.AlterField(
            model_name='hotelowner',
            name='hotel_ownership_documents',
            field=models.FileField(upload_to='media/ownership_documents/'),
        ),
        migrations.AlterField(
            model_name='hotelowner',
            name='profile_picture',
            field=models.ImageField(upload_to='media/profile_pictures/'),
        ),
    ]
