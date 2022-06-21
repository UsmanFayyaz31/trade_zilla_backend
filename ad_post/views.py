from rest_framework import generics
from django.http import JsonResponse
from rest_framework import status
from ad_post.models import AdPost
from ad_post.serializers import AdPostSerializer


class AdPostViewSet(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        data = list(AdPost.objects.all().values())
        return JsonResponse({'data': data})

    def post(self, request, *args, **kwargs):
        ad_post = AdPostSerializer(data=request.data)

        if ad_post.is_valid():
            ad_post.save()
            return JsonResponse(data=ad_post.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
