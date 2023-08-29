from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.seller_profile,name='sellerProfile'),
    path('profile/product-manager/create', views.create_product, name='productManager'),
    path('profile/product-manager/detail/<int:type>/<int:id>', views.product_detail, name='productDetail'),
    path('profile/product-manager/delete/<int:id>', views.product_delete, name='productDelete'),
]