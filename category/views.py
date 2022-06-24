from rest_framework import generics
from django.http import JsonResponse
from category.models import Category


# Create your views here.
class ListOfCategories(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        data = list(Category.objects.all().values('label', 'id'))
        return JsonResponse({'data': data})
