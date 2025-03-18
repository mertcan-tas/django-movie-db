from django.core.management.base import BaseCommand
from project.models import Movie
from django.utils import termcolors
from faker import Faker

class Command(BaseCommand):
    help = "Adds data to the Province model"

    def handle(self, *args, **kwargs):
        movie_list = [

            {
                "title": "Spider-Man: No Way Home",
                "original_title": "Spider-Man: No Way Home",
                "release_year": 2021,
                "plot": "Adana",
                "poster": "Adana",
                "runtime": "Adana",
                "director": "Adana",
                "actors": "Adana",
                "runtime": "imdb_rating"
            },
        ]

        for movie in movie_list:
            try:
                Movie.objects.create(**movie_list)
                #self.stdout.write(self.style.SUCCESS(f"[+] Movie added. Province: {movie.title}"))
            except Exception as e:
                #self.stdout.write(self.style.ERROR(f"[+] Failed to add province. Movie: {str(e)}"))
                self.stdout.write(termcolors.make_style(fg="red")(f"✘ {str(e)}"))

        self.stdout.write(self.style.SUCCESS('✔ All provinces created successfully!'))
