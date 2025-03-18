from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='actors/', null=True, blank=True)

    def __str__(self):
        return self.name
