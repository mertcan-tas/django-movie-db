from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import termcolors


class Command(BaseCommand):
    help = 'Creates a superuser with predefined data'

    def handle(self, *args, **kwargs):
        UserModel = get_user_model()
        username = "mertcan"
        email = "admin@admin.com"
        password = "password"
        
        try:
            if not UserModel.objects.filter(email=email).exists():
                user = UserModel.objects.create_superuser(email=email, username=username, password=password)
                user.is_active = True
                user.is_staff = True
                user.save()

                self.stdout.write(self.style.SUCCESS('✔ User created successfully!'))
            else:
                self.stdout.write(self.style.WARNING('✘ Superuser already exists!'))

        except Exception as e:
            self.stdout.write(termcolors.make_style(fg="red")(f"✘ {str(e)}"))
