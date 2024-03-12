import random

from django.core.management.base import BaseCommand
from myapp2.models import User_ht, Product_ht
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Generate fake user_ht and products_ht."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user_ht = User_ht(name=fake.first_name(), email=fake.unique.email(), phone=fake.phone_number(), address=fake.address())
            print(user_ht)
            user_ht.save()
            # for j in range(1, count + 1):
            #     product_ht = Product_ht(name=f'Product_name{j}', price=random.randint(0, 100),
            #                             description=fake.text(10), quantity=random.randint(0, 20))
            #     product_ht.save()
