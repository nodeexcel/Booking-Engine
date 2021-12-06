from django.urls import path
from listings.views import  GetBookingInfoView
urlpatterns = [
    path("units/", GetBookingInfoView.as_view()),
]