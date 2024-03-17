from django.shortcuts import render
from django.urls import path

from .views import products_ordered_by_user, hello

urlpatterns = [
    path('by_user/<int:user_ht_id>/<int:q_day>/', products_ordered_by_user, name='by_user'),
    path('hello/', hello, name='hello'),


]
