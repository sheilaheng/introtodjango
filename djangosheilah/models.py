from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField(default=1)
    age = models.IntegerField()
    gender = models.CharField(max_length=30, blank=False, null=False)
    country = models.CharField(max_length=30, blank=False, default="Kenya")
    city = models.CharField(max_length=30, blank=False, default="Nairobi")


def __str__(self):
    return self.name
