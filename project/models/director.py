from django.db import models
from django.urls import reverse

class Director(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='directors/', null=True, blank=True)

    def __str__(self):
        return self.name
