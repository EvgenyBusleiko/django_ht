from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age:{self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    lastname = models.CharField(max_length=100)
    biography = models.TextField()
    date_of_birth = models.DateTimeField(default=timezone.now())

    @property
    def full_name(self):
        return f'Полное имя {self.name} {self.lastname}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'Title is {self.title}'


class User_ht(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone:{self.phone}, addres:{self.address}, reg_date:{self.reg_date}'


class Product_ht(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField(max_length=8)
    date_created = models.DateTimeField(auto_now_add=True)

    # image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, description:{self.description},  quantity:{self.quantity}, date_created:{self.date_created}'


class Order_ht(models.Model):
    customer = models.ForeignKey(User_ht, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'customer: {self.customer},  total_price:{self.total_price}, date_ordered:{self.date_ordered}'

class order_ht_product_ht(models.Model):
    order = models.ForeignKey(Order_ht, on_delete=models.CASCADE)
    product = models.ForeignKey(Product_ht, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=8)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'product: {self.product},  quantity:{self.quantity}, date_created:{self.date_created}'
