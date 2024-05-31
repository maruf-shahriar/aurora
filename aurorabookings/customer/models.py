from django.db import models
from hotel_owner.models import Hotel, Room, HotelOwner
from django.contrib.auth import get_user_model

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cell = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    visited_u = models.IntegerField()  # assuming visited_u is a count of visited places
    description = models.TextField()
    nid_passport_number = models.CharField(max_length=20, default='default_value')
    
    def __str__(self):
        return self.name

User = get_user_model()

class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('Not Confirmed', 'Not Confirmed'),
        ('Confirmed', 'Confirmed'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    members = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_status = models.CharField(max_length=15, choices=BOOKING_STATUS_CHOICES, default='Not Confirmed')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Booking {self.id} by {self.customer} for {self.hotel}'