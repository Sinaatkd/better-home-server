from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'create an admin user'
    
    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+', type=str)
        parser.add_argument('password', nargs='+', type=str)
        parser.add_argument('phone_number', nargs='+', type=str)
    
    
    def handle(self, *args, **kwargs):
        username = kwargs['username'][0]
        password = kwargs['password'][0]
        phone_number = kwargs['phone_number'][0]
        user = User(username=username, phone_number=phone_number, is_staff=True, is_superuser=True)
        user.set_password(password)
        try:
            user.save()
            self.stdout.write(self.style.SUCCESS(f'User "{username}" Created'))
        except:
            raise CommandError('Phone Number or username Already taken')