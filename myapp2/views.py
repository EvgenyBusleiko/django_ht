from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Product_ht, User_ht, Order_ht, order_ht_product_ht, Shooter
from .forms import Product_htForm, ShoterForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


def hello(request):
    return HttpResponse("Hello World from function!")


def products_ordered_by_user(request, user_ht_id, q_day):
    user_ht = get_object_or_404(User_ht, pk=user_ht_id)

    date = datetime.now() - timedelta(days=q_day)

    orders = Order_ht.objects.filter(customer=user_ht_id, date_ordered__lte=date)
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


def product_form_ht(request):
    if request.method == 'POST':
        form = Product_htForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            quantity = form.cleaned_data['quantity']
            date_created = form.cleaned_data['data']
            image = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product_ht(name=name, price=price, description=description, quantity=quantity,
                                 date_created=date_created)
            product.save()
    else:
        form = Product_htForm()
    return render(request, 'myapp2/product_ht_form.html', {'form': form})


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ShoterForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            # Get the current instance object to display in the template
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            extention=image.name.split('.')[1]

            filename = f'{title.replace(" ","_")}{datetime.now().date()}.{extention}'
            fs.save(filename, image)
            file_url = fs.url(filename)
            return render(request, 'myapp2/shooter.html', {'form': form, 'file_url': file_url})
    else:
        form = ShoterForm()
    return render(request, 'myapp2/shooter.html', {'form': form})


class CreateShooterView(CreateView):  # новый
    model = Shooter
    form_class = ShoterForm
    template_name = 'add_shooter.html'
    success_url = reverse_lazy('shooter')
