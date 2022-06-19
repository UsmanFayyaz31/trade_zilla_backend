from django.urls import path
from location.views import ListOfLocations

urlpatterns = [
    path('', ListOfLocations.as_view(), name='get_location')
]
