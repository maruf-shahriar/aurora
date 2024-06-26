# Generated by Django 5.0.6 on 2024-05-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelOwner',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('hotel_ownership_documents', models.FileField(upload_to='ownership_documents/')),
                ('address_proof', models.FileField(upload_to='address_proof/')),
            ],
        ),
    ]
