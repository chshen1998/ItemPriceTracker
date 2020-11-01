from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=120)
    shop = models.CharField(max_length=25)
    current_price = models.FloatField()
    lowest_price = models.FloatField()
    original_price = models.FloatField()
    link = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def Item(self, name, shop, price, link):
        self.name = name
        self.shop = shop
        self.current_price = price
        self.lowest_price = price
        self.original_price = price
        self.link = link

