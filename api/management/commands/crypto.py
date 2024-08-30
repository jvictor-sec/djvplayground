import base64
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Encrypt or decrypt a credential using Base64"

    def add_arguments(self, parser):
        parser.add_argument('credential', type=str, help='The credential to be processed')

        parser.add_argument(
            '--decrypt',
            action='store_true',
            help='Use this flag to decrypt the input credential (default is encrypt)'
        )

    def handle(self, *args, **options):
        credential = options['credential']

        if options['decrypt']:
            try:
                decoded_string = base64.b64decode(credential.encode('utf-8')).decode('utf-8')
                self.stdout.write(self.style.SUCCESS('Decrypted credential: %s' % self.style.WARNING(decoded_string)))
            except Exception as e:
                raise CommandError('Error during decryption: %s' % str(e))
        else:
            encoded_string = base64.b64encode(credential.encode('utf-8')).decode('utf-8')
            self.stdout.write(self.style.SUCCESS('Encrypted credential: %s' % self.style.WARNING(encoded_string)))
