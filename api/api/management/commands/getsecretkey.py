from django.core.management.base import BaseCommand, CommandError
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = "Generate Django's Secret Key"

    def handle(self, *args, **options):
        secret_key = get_random_secret_key()

        self.stdout.write(self.style.SUCCESS('Secret key generated: %s' % self.style.WARNING(secret_key)))