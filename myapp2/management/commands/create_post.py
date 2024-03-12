import decimal

from django.core.management.base import BaseCommand
from myapp2.models import User_ht, Order_ht, Product_ht


class Command(BaseCommand):
    help = "Create post."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID')
        parser.add_argument('product', type=int, help='Product_ID')
        parser.add_argument('total_price', type=decimal, help='total_price')


    def handle(self, *args, **kwargs):
        user = User_ht.objects.get(pk=kwargs.get('pk'))
        product=Product_ht.objects.get(product=kwargs.get('product'))
        order =Order_ht(customer=user,products=product, total_price=kwargs['total_price'])

        order.save()
        self.stdout.write(f'{order}')
