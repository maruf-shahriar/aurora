from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet,BookingViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]