




from django.contrib.auth.admin import User
from django.core.management import BaseCommand
import random

class Command(BaseCommand):


    # def add_arguments(self, parser):
    #     parser.add_argument('person',type=int,help='indicate the no of Users created')
    #
    #
    #     parser.add_argument('-p', '--prefix', type=str, help='indicate the no of Users created')
    #
    #     parser.add_argument('-a','--admin',action='store_true')

    def handle(self, *args, **options):
        self.stdout.write("This is from  praful")
        # person=options['person']
        # prefix=options['prefix']
        #
        #
        #
        # admin=options['admin']
        # for item in range(person):
        #
        #     ran=random.randint(100,300)
        #     if prefix:
        #         uname=prefix+'name'+str(ran)
        #         #User.objects.create_user(username=prefix+'name'+str(ran),email='NewUser'+str(ran)+'@gmail.com',password=random.randint(1000,2000))
        #     else:
        #         uname='name'+str(ran)
        #     if admin:
        #         User.objects.create_superuser(username=uname,email='NewUser'+str(ran)+'@gmail.com',password=random.randint(1000,2000))
        #     else:
        #         User.objects.create_user(username=uname,email='NewUser'+str(ran)+'@gmail.com',password=random.randint(1000,2000))
        #
