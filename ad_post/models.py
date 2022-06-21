from django.db import models
from users.models import User
from location.models import Location


# Create your models here.
class AdPost(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    item_required = models.TextField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return self.product_name


class ExchangeWithRequests(models.Model):
    exchanged_with = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(AdPost, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
