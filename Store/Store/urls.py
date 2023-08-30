
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("Accounts.urls")),
    path('seller/', include("Seller.urls")),
    path('', include("customer.urls")),
    
]
