from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, HotelOwnerViewSet, RoomViewSet

router = DefaultRouter()
router.register(r'hotel_owners', HotelOwnerViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]