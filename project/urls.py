from django.urls import path
from project.views import HomeView, MovieListview

urlpatterns = [
    path('', HomeView, name='home'),
    path('movies/', MovieListview, name='movies')
]
