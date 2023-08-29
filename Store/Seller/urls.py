from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.seller_profile,name='sellerProfile'),
    path('profile/product-manager/', views.product_manager, name='productManager'),
    path('profile/product-manager/create', views.create_product, name='productCreate'),
    path('profile/product-manager/update/<int:id>', views.update_product, name='productUpdate'),
    path('profile/product-manager/delete/<int:id>', views.delete_product, name='productDelete'),
]