from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.customer_profile,name='customerProfile'),
    path('', views.home,name='home'),

    path('products/', views.show_products, name='products'),
    path('products/select/<int:id>', views.select, name='select'),
    path('products/detail/<int:id>', views.product_detail, name='productDetail'),
    path('cart/', views.show_cart, name='cart'),
    path('cart/order/', views.order, name='order'),
    path('orders/', views.show_orders, name='customerOrders'),
]