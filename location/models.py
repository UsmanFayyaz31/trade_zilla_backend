from django.db import models


# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.city
