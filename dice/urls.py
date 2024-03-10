from django.urls import path
from . import views

urlpatterns = [
    path('dice/', views.dice, name='index'),
    path('coin/<int:amount_flips>', views.coin, name='about'),
    path('hundred/', views.hundred, name='about'),

]
