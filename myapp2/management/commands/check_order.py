from django.core.management.base import BaseCommand
from myapp2.models import User_ht, Order_ht, Product_ht, order_ht_product_ht
from decimal import Decimal


class Command(BaseCommand):
    help = "Check order"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='OrderID')
        # self.stdout.write(f'{pk}')

    def handle(self, *args, **kwargs):


        products = order_ht_product_ht.objects.filter(order=kwargs['id'])
        self.stdout.write(f'{products}')
