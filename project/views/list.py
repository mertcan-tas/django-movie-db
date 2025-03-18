from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page

from project.models import Movie

#@cache_page(60 * 15)
def MovieListview(request):
    movies = Movie.published.all()

    return render(
        request,
        'list.html',
        {'movies': movies}
    )
