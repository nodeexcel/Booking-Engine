from rest_framework import serializers
from .models import Listing
class BookingSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=30, decimal_places=2)
    class Meta:
        model = Listing
        fields = "__all__"
