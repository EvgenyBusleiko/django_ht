from django.core.management.base import BaseCommand
from myapp2.models import User_ht


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **kwargs):
        users = User_ht.objects.all()
        self.stdout.write(f'{users}')
