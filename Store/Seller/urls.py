from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.seller_profile,name='sellerProfile'),
    path('product-manager/', views.ProductManager.as_view(), name="productManager"),
    path('product-manager/create/', views.CreateProduct.as_view()),
    path('product-manager/update/<int:id>', views.update_Product, name='productUpdate'),
    path('product-manager/delete/<int:id>', views.delete_product, name='productDelete'),
    path('product-manager/create/category/',views.SetCategory.as_view()),
    path('orders/', views.show_orders, name='sellerOrders'),
]