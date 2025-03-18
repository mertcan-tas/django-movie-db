import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
from django.utils import termcolors

class Command(BaseCommand):
    help = 'Proje temizleme ve veritabanı sıfırlama'

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput', '--no-input',
            action='store_false',
            dest='interactive',
            help='Onay sormadan direkt çalıştır',
        )

    def handle(self, *args, **options):
        success_style = termcolors.make_style(fg="green")
        error_style = termcolors.make_style(fg="red")
        running_style = termcolors.make_style(fg="blue", opts=("bold",))

        # 1. Dosya ve klasör temizliği
        self.stdout.write(running_style("\n→ Proje temizliği yapılıyor..."))
        deleted_items = self.clean_project_files()
        
        if deleted_items["pycache"]:
            self.stdout.write(success_style(f"✔ pycache'ler silindi ({deleted_items['pycache']} adet)"))
        if deleted_items["migrations"]:
            self.stdout.write(success_style(f"✔ migrationlar silindi ({deleted_items['migrations']} adet)"))

        # 2. Veritabanı temizliği
        self.stdout.write(running_style("\n→ Veritabanı temizliği yapılıyor..."))
        self.clean_databases(options['interactive'])

    def clean_project_files(self):
        target_dir = getattr(settings, 'BASE_DIR', '.')
        counters = {"pycache": 0, "migrations": 0}

        for root, dirs, _ in os.walk(target_dir):
            if 'env' in dirs:
                dirs.remove('env')
                
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if dir_name == "__pycache__":
                    shutil.rmtree(dir_path, ignore_errors=True)
                    counters["pycache"] += 1
                elif dir_name == "migrations":
                    shutil.rmtree(dir_path, ignore_errors=True)
                    counters["migrations"] += 1

        return counters

    def clean_databases(self, interactive):
        # SQLite temizliği
        db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        if os.path.exists(db_path):
            os.remove(db_path)
            self.stdout.write(termcolors.make_style(fg="green")(f"✔ SQLite veritabanı silindi"))

        # PostgreSQL temizliği
        if interactive:
            confirm = input('\nTüm PostgreSQL tabloları silinecek! Onaylıyor musunuz? [y/N]: ')
            if confirm.lower() != 'y':
                return

        with connection.cursor() as cursor:
            try:
                cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
                self.stdout.write(termcolors.make_style(fg="green")(f"✔ Tüm PostgreSQL tabloları silindi"))
            except Exception as e:
                self.stdout.write(termcolors.make_style(fg="red")(f"✘ {str(e)}"))