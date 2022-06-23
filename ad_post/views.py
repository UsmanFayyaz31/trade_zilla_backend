from rest_framework import generics, permissions
from django.http import JsonResponse
from rest_framework import status
from ad_post.models import AdPost, ExchangeRequest
from ad_post.serializers import AdPostSerializer, ExchangeRequestSerializer
from rest_framework import parsers


class AdPostViewSet(generics.ListCreateAPIView):
    queryset = ExchangeRequest.objects.all()
    serializer_class = AdPostSerializer

    def get(self, request, *args, **kwargs):
        ad_posts = list(self.queryset.values())

        for ad_post in ad_posts:
            exchange_requests = list(
                self.queryset.filter(product=ad_post["id"]).values('exchange_with', 'user__email'))
            ad_post['exchange_with_requests'] = exchange_requests

        return JsonResponse({'data': ad_posts})

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(data={"errors": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExchangeRequestViewSet(generics.CreateAPIView):
    serializer_class = ExchangeRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(data={"errors": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
