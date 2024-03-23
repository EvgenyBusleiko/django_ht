from django.shortcuts import render
from django.urls import path
from .views import image_upload_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

from .views import products_ordered_by_user, hello, product_form_ht, product_upload_view,show_all_product,product_full
from . import views


urlpatterns = [
    path('by_user/<int:user_ht_id>/<int:q_day>/', products_ordered_by_user, name='by_user'),
    path('hello/', hello, name='hello'),
    path('add_product/', product_upload_view, name='add_product'),
    path('shooter/', image_upload_view, name='Shooter'),
    path('add/', product_upload_view, name='add'),
    path('main_page/', views.main_page, name='main_page'),
    path('show_all_product/', show_all_product, name='show_all_product'),
    path('product_full/<int:post_id>/', product_full, name='product_full'),

    # path('create_shooter/', CreateShooterView.as_view(), name='CreateShooterView'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
