from django.db import models
from django.conf import settings
from project.models import Movie

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s watchlist: {self.movie.title}"

    class Meta:
        unique_together = ('user', 'movie')
