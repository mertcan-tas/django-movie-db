from django.db import models
from project.models import Movie, Actor

class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.actor.name} as {self.character_name} in {self.movie.title}"

    class Meta:
        unique_together = ('movie', 'actor', 'character_name')
