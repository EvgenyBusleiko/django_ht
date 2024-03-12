from django.shortcuts import render
import logging
from django.shortcuts import render


def index(request):
    return render(request, 'myapps/index.html',{'title':'Главная страница'})


def about(request):
    return render(request, 'myapps/about.html',{'title':'О нас'})
