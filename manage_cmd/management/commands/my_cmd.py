





from django.core.management.base import BaseCommand,CommandError
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

