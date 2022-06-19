from rest_framework import generics
from django.http import JsonResponse
from location.models import Location


class ListOfLocations(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        data = list(Location.objects.all().values('city', 'id'))
        return JsonResponse({'data': data})
