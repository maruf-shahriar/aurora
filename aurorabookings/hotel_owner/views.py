from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Hotel, HotelOwner, Room
from .serializers import HotelSerializer, HotelOwnerSerializer, RoomSerializer

class HotelOwnerViewSet(viewsets.ModelViewSet):
    queryset = HotelOwner.objects.all()
    serializer_class = HotelOwnerSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(detail=False, methods=['post'], url_path='bulk_create')
    def bulk_create(self, request):
        hotel_id = request.data.get('hotel_id')
        rooms_data = request.data.get('rooms', [])

        if not hotel_id or not rooms_data:
            return Response({"error": "hotel_id and rooms data are required"}, status=status.HTTP_400_BAD_REQUEST)

        hotel = Hotel.objects.get(pk=hotel_id)
        created_rooms = []

        for room_data in rooms_data:
            room_number = hotel.rooms.count() + 1
            room_data['hotel'] = hotel_id
            room_data['room_number'] = room_number
            serializer = RoomSerializer(data=room_data)
            if serializer.is_valid():
                serializer.save()
                created_rooms.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(created_rooms, status=status.HTTP_201_CREATED)