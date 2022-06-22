from django.urls import path
from ad_post.views import AdPostViewSet, ExchangeRequestViewSet

urlpatterns = [
    path('/', AdPostViewSet.as_view(), name='ad_post'),
    path('/exchange_requests/', ExchangeRequestViewSet.as_view(), name='exchange_requests'),
]
