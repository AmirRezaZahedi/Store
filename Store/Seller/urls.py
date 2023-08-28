from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.seller_profile,name='sellerProfile'),
    path('profile/detail/<int:type>/<int:id>', views.product_detail, name='productDetail')
]