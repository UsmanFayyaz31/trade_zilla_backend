from django.urls import path
from .views import SignupAPIView, EmailTokenObtainPairView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),

]
