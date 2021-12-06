from django.db.models import Min
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from .app_filters import Booking_Filter
from .models import BookingInfo, Listing
from .serializers import BookingSerializer


class GetBookingInfoView(ListAPIView):
    queryset = (
        BookingInfo.objects.all().select_related(
            "hotel_room_type", "listing").prefetch_related(
            "booking")
    )
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = Booking_Filter
    ordering = ['-price']
    def filter_queryset(self, queryset):
        return Listing.objects.filter(pk__in=super().filter_queryset(queryset).values('listing')).annotate(price=Min('booking_info__price'))