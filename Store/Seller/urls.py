from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.seller_profile,name='sellerProfile'),
    path('product-manager/', views.product_manager, name='productManager'),
    path('product-manager/create', views.create_product, name='productCreate'),
    path('product-manager/update/<int:id>', views.update_Product, name='productUpdate'),
    path('product-manager/delete/<int:id>', views.delete_product, name='productDelete'),
]