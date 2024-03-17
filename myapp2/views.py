from datetime import datetime, timedelta

from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Product_ht, User_ht, Order_ht, order_ht_product_ht
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World from function!")


def products_ordered_by_user(request, user_ht_id, q_day):
    user_ht = get_object_or_404(User_ht, pk=user_ht_id)

    date = datetime.now() - timedelta(days=q_day)

    orders = Order_ht.objects.filter(customer=user_ht_id,date_ordered__lte=date)
    names = set()
    for order in orders:
        print(order.id)
        product = order_ht_product_ht.objects.filter(order=order.id)
        for pr in product:
            names.add(pr.product.name)
            print(pr.product.name)
    context = {
        'user_ht': user_ht.name,
        'product': names,
        'days': q_day,
    }

    return render(request, 'myapp2/by_user.html', context)
