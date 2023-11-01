from django.urls import path
from . import views







urlpatterns = [
    
    path('register/', views.register,name='register'),
    path('register/seller/', views.seller_register,name='sellerRegister'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout_view, name='logout'),
]