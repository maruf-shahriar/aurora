# Generated by Django 5.0.6 on 2024-05-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='nid_passport_image',
        ),
        migrations.AddField(
            model_name='customer',
            name='nid_passport_number',
            field=models.CharField(default='default_value', max_length=20),
        ),
    ]
