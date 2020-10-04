from django.db import models
from django.views import generic

class Item(models.Model):
    item_name = models.CharField(max_length=100, primary_key=True)
    price = models.IntegerField()
    in_cart = models.BooleanField()

    def __str__(self):
        return self.item_name

