from django.urls import path
from . import views
from django.urls.conf import include
from rest_framework_nested import routers

router = routers.DefaultRouter()

urlpatterns = [

    path(r'', include(router.urls)),

    path('profile/', views.customer_profile,name='customerProfile'),
    path('', views.home,name='home'),

    path('products/', views.show_products, name='products'),
    path('products/select/<int:id>', views.select, name='select'),
    path('products/detail/<int:id>', views.product_detail, name='productDetail'),
    path('cart/', views.show_cart, name='cart'),
    path('cart/update/<int:id>', views.update_cart, name='updateCart'),
    path('cart/delete/<int:id>', views.delete_cart, name='deleteCart'),
    path('orders/', views.show_orders, name='customerOrders'),
    path('update_cart/<int:id>/', views.update_cart, name='update_cart'),
    path('address/', views.fill_address, name='address')

]