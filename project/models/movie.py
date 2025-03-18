from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from taggit.managers import TaggableManager
from project.models import Director, Actor
from shortuuid.django_fields import ShortUUIDField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Movie.Status.PUBLISHED)
        )




class Movie(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    id = ShortUUIDField( length=10, max_length=10, alphabet="123456789", primary_key=True, editable=False, unique=True )

    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200, blank=True)
    release_year = models.IntegerField()
    plot = models.TextField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    runtime = models.IntegerField(help_text="Time")
    imdb_rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name="actors")

    genres = TaggableManager
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager() #

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    class Meta:
        ordering = ['-release_year', 'title']
        indexes = [
            models.Index(fields=['release_year']),
            models.Index(fields=['title']),
        ]
