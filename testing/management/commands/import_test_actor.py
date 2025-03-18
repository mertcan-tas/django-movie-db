import random
from datetime import datetime, timedelta
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from lorem_text import lorem

from project.models import Director

from faker import Faker

fake = Faker()
User = get_user_model()

class Command(BaseCommand):
    help = 'Random create actor'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, default=100, help='Director Count')

    def handle(self, *args, **options):
        total = options['total']

        for _ in range(total):
            advert = Director(
                name=fake.name(),
                bio=lorem.paragraphs(1),
                birth_date=timezone.now(),
            )

            advert.save()

        self.stdout.write(self.style.SUCCESS(f'✔ {total} test advert created successfully!'))
