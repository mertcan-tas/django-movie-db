from django import template
from project.models import Movie
from django.core.cache import cache

register = template.Library()

@register.simple_tag
def total_movies():
    total_count = cache.get_or_set("total_movies", Movie.published.count(), 60 * 15)
    return total_count
