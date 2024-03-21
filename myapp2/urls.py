from django.shortcuts import render
from django.urls import path
from .views import image_upload_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

from .views import products_ordered_by_user, hello, product_form_ht

urlpatterns = [
    path('by_user/<int:user_ht_id>/<int:q_day>/', products_ordered_by_user, name='by_user'),
    path('hello/', hello, name='hello'),
    path('add_product/', product_form_ht, name='add_product'),
    path('shooter/', image_upload_view, name='Shooter'),

    # path('create_shooter/', CreateShooterView.as_view(), name='CreateShooterView'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
