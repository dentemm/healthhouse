import os

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

	help = 'Prints os'

	def handle(self, *args, **options):

		self.stdout.write(self.style.SUCCESS(os.environ))
