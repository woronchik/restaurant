from django.core.management.base import BaseCommand
import sqlite3
from sqlite3 import Error


class Command(BaseCommand):
    help = 'Create a SQLite database'

    def add_arguments(self, parser):
        parser.add_argument('db_file', type=str)

    def handle(self, *args, **options):
        db_file = options['db_file']
        self.create_connection(db_file)

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            self.stdout.write(self.style.SUCCESS(f"SQLite version: {sqlite3.version}"))
        except Error as e:
            self.stdout.write(self.style.ERROR(e))
        finally:
            if conn:
                conn.close()