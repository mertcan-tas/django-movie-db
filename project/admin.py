from django.contrib import admin

from project.models import (
    Director,
    Actor,
    Movie,
    MovieCast,
    Review,
    Watchlist,
)


admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieCast)
admin.site.register(Review)
admin.site.register(Watchlist)
