import datetime

from django import forms
from .models import Shooter

# class Author(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     lastname = forms.CharField(max_length=100)
#     biography = forms.CharField(widget=forms.Textarea)
#     data_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     content = forms.CharField(widget=forms.Textarea)
#     date = forms.DateTimeField()
#     author = forms.ModelChoiceField(queryset=Author.objects.all())
#     is_published = forms.BooleanField()
#     views = forms.IntegerField(default=0)

class Product_htForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description = forms.CharField()
    quantity = forms.IntegerField()
    date_created = forms.DateField(initial=datetime.date.today())
    image = forms.ImageField()


class ShoterForm(forms.Form):
    title =forms.CharField(max_length=50)
    image = forms.ImageField()