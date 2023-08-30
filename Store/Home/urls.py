from django.urls import path
from . import views

urlpatterns = [
    path('seller/profile/', views.seller_profile,name='sellerProfile'),
    path('customer/profile/', views.customer_profile,name='customerProfile'),
]