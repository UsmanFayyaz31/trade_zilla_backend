from django.urls import path
from category.views import ListOfCategories

urlpatterns = [
    path('', ListOfCategories.as_view(), name='get_category')
]
