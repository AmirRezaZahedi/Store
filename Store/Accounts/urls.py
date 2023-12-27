from django.urls import path
from . import views
from django.urls.conf import include
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('customer', views.CustomerViewSet,basename='customer')
router.register('seller', views.SellerViewSet,basename='seller')



urlpatterns = [
   
    path(r'', include(router.urls)),

]