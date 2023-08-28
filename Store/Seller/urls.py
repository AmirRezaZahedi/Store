from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.seller_profile,name='sellerProfile'),
    path('product-manager/', views.product_manager, name='productManager'),
    path('product-manager/detail/<int:type>/<int:id>', views.product_detail, name='productDetail'),
    path('product-manager/delete/<int:id>', views.product_delete, name='productDelete'),
]