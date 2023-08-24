from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('register/seller/', views.seller_register,name='seller_register'),
    path('login/', views.login,name='login'),
]