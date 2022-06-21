from django.urls import path
from ad_post.views import AdPostViewSet

urlpatterns = [
    path('/', AdPostViewSet.as_view(), name='get_ad_post')
]
