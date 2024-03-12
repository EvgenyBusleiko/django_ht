from django.core.management.base import BaseCommand
from myapp2.models import User_ht, Order_ht, Product_ht, order_ht_product_ht
from decimal import Decimal

class Command(BaseCommand):
    help = "Add product to order"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='OrderID')
        parser.add_argument('id', type=int, help='Product_ID')
        parser.add_argument('p_quantity', type=int, help='quantity')

    def handle(self, *args, **kwargs):

        order_id = Order_ht.objects.latest('pk')

        product=Product_ht.objects.get(id=kwargs.get('id'))
        product_order = order_ht_product_ht(order=order_id, product=product, quantity=kwargs['p_quantity'])
        product_order.save()


        self.stdout.write(f'{product_order}')