




from django.contrib.auth.admin import User
from django.core.management import BaseCommand
import random

class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument('person',type=int,help='indicate the no of Users created')


    def handle(self, *args, **options):
        person=options['person']
        for item in range(person):
            ran=random.randint(100,300)
            User.objects.create_user(username='name'+str(ran),email='NewUser'+str(ran)+'@gmail.com',password=random.randint(1000,2000))
