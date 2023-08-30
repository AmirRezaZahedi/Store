from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.customer_profile,name='customerProfile'),
    path('', views.home,name='home'),

    path('products/', views.show_products, name='products'),
    path('products/order/<int:id>/<int:number>', views.order, name='order'),
    path('products/detail/<int:id>', views.product_detail, name='productDetail'),
]