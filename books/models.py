from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    topic = models.CharField(max_length=200)
    def __str__(self):
        return self.title





