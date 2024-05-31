from rest_framework import serializers
from .models import Customer,Booking
from hotel_owner.models import Room

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    room_number = serializers.ReadOnlyField(source='room.room_number')
    room_type = serializers.ReadOnlyField(source='room.room_type')
    hotel_name = serializers.ReadOnlyField(source='hotel.name')
    customer_name = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Booking
        fields = ['id', 'hotel', 'customer', 'room', 'room_number', 'room_type', 'members', 'check_in_date', 'check_out_date', 'booking_status', 'payment_status', 'special_request', 'hotel_name', 'customer_name']
        read_only_fields = ['booking_status', 'hotel', 'customer']