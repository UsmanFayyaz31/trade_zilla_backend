from rest_framework import generics
from django.http import JsonResponse
from rest_framework import status
from ad_post.models import AdPost, FavoriteProduct
from ad_post.serializers import AdPostSerializer, ExchangeRequestSerializer, FavoriteProductSerializer


class FavoriteProductViewSet(generics.GenericAPIView):
    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoriteProductSerializer

    def get(self, request, *args, **kwargs):
        if request.GET['user_id']:
            response = list(self.queryset.filter(user_id=request.GET['user_id'])
                            .values('id', 'product__product_name', 'product__product_image', 'product__item_required',
                                    'product__address'))

            for res in response:
                res['product__product_image'] = 'https://tradezillaimages.s3.amazonaws.com/' + res['product__product_image']

            return JsonResponse(data=response, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(data={'errors': 'User Id not provided.'}, status=status.HTTP_400_BAD_REQUEST,
                                safe=False)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data={'details': 'Added to Favorites.'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(data={"errors": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        if request.GET['favorite_id']:
            delete_product = FavoriteProduct.objects.filter(id=request.GET['favorite_id']).delete()
            if delete_product[0]:
                return JsonResponse(data={"details": "Deleted."}, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(data={"details": "Not Found"}, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(data={'errors': 'Favorite Id not provided.'}, status=status.HTTP_400_BAD_REQUEST,
                                safe=False)


class AdPostViewSet(generics.ListCreateAPIView):
    queryset = AdPost.objects.all()
    serializer_class = AdPostSerializer

    def get(self, request, *args, **kwargs):
        location_id = request.GET.get('location_id', None)
        category_id = request.GET.get('category_id', None)

        filters = dict()
        if location_id:
            filters.update(location_id=location_id)

        if category_id:
            filters.update(category_id=category_id)

        ad_posts = list(
            self.queryset.select_related('exchange_with').filter(**filters).values('product_image', 'product_name',
                                                                                   'description',
                                                                                   'item_required', 'id',
                                                                                   'user__email', 'location__city',
                                                                                   'category__label'))

        for ad_post in ad_posts:
            exchange_requests = list(
                self.queryset.filter(id=ad_post["id"]).values('exchangerequest__exchange_with', 'user__email'))
            ad_post['exchange_with_requests'] = exchange_requests
            ad_post['product_image'] = 'https://tradezillaimages.s3.amazonaws.com/' + ad_post['product_image']

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
