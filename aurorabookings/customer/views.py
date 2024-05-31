from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Customer, Booking
from .serializers import CustomerSerializer, BookingSerializer
from rest_framework.response import Response
from hotel_owner.models import Hotel, Room

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        hotel_id = request.data.get('hotel')
        customer_id = request.user.id
        room_id = request.data.get('room')

        if not hotel_id or not room_id:
            return Response({"error": "Hotel ID and Room ID are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            hotel = Hotel.objects.get(pk=hotel_id)
            room = Room.objects.get(pk=room_id)
        except Hotel.DoesNotExist:
            return Response({"error": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        booking_data = request.data.copy()
        booking_data['hotel'] = hotel.id
        booking_data['customer'] = customer_id
        booking_data['room'] = room.id
        booking_data['booking_status'] = 'Not Confirmed'

        serializer = self.get_serializer(data=booking_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if 'booking_status' in request.data and not request.user.is_staff:
            return Response({"error": "Only hotel owners can change booking status"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
