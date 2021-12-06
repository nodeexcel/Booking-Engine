from django.db.models import Q
from django_filters import DateFromToRangeFilter, NumberFilter
from django_filters.rest_framework import FilterSet
from listings.models import BookingInfo
class Booking_Filter(FilterSet):
    available_dates = DateFromToRangeFilter(
        label="Check_in & Check_out dates", method="dates_check"
    )
    max_price = NumberFilter(field_name="price", lookup_expr="lte")
    def dates_check(self, queryset,name,date):
        return queryset.exclude(
            Q(booking__check_in_date__range=(date.start, date.stop),)
            |Q(booking__check_out_date__range=(date.start, date.stop),)
        )
    class Meta:
        model = BookingInfo
        fields = [
            "available_dates",
            "max_price",
        ]