from django.db import models

class HotelOwner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/')
    hotel_ownership_documents = models.FileField(upload_to='media/ownership_documents/')
    address_proof = models.FileField(upload_to='media/address_proof/')
    
    def __str__(self):
        return self.name

class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number_of_rooms = models.IntegerField()
    images = models.ImageField(upload_to='media/hotel_image/')  # Store images as JSON (list of URLs or paths)
    facilities = models.TextField()
    promo = models.CharField(max_length=100)
    area_or_location = models.CharField(max_length=255)
    owner = models.ForeignKey(HotelOwner, on_delete=models.CASCADE, related_name='hotels')
    
    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    ]
    
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.hotel.name} - Room {self.room_number} ({self.room_type})'