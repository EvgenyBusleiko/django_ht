from django.urls import path
from . import views

urlpatterns = [
    path('dice/<int:amount_flips>', views.dice, name='dice'),
    path('coin/<int:amount_flips>', views.coin, name='coin'),
    path('hundred/<int:amount_gens>', views.hundred, name='hundred'),

]
