from rest_framework import generics
from django.http import JsonResponse
from rest_framework import status
from ad_post.models import AdPost, ExchangeRequest
from ad_post.serializers import AdPostSerializer, ExchangeRequestSerializer


class AdPostViewSet(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        ad_posts = list(AdPost.objects.all().values())

        for ad_post in ad_posts:
            exchange_requests = list(
                ExchangeRequest.objects.filter(product=ad_post["id"]).values('exchange_with', 'user__email'))
            ad_post['exchange_with_requests'] = exchange_requests

        return JsonResponse({'data': ad_posts})

    def post(self, request, *args, **kwargs):
        ad_post = AdPostSerializer(data=request.data)

        if ad_post.is_valid():
            ad_post.save()
            return JsonResponse(data=ad_post.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)


class ExchangeRequestViewSet(generics.RetrieveAPIView):
    def post(self, request, *args, **kwargs):
        exchange_request = ExchangeRequestSerializer(data=request.data)

        if exchange_request.is_valid():
            exchange_request.save()
            return JsonResponse(data=exchange_request.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
