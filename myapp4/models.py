from django.db import models
class User4(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, age:{self.age}'


# Create your models here.
