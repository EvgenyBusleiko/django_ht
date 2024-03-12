from django.core.management.base import BaseCommand
from myapp2.models import User_ht
class Command(BaseCommand):
    help = "Get user_ht by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']

        user = User_ht.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')