from django.db import models
from django.contrib.auth.models import User
import datetime


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, null=False, blank=False)
    description = models.TextField()
    created_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name