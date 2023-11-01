from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('category', views.CategoryViewSet, basename='category')
router.register('orders', views.OrdersViewSet, basename='orders')

field_router = routers.NestedDefaultRouter( router, 'category', lookup='category')
field_router.register('fields', views.FieldsViewSet,basename='category-fields')





urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(field_router.urls)),
    #path('profile/', views.seller_profile,name='sellerProfile'),
    #path('product-manager/', views.ProductManager.as_view(), name="productManager"),
    #path('product-manager/create/', views.CreateProduct.as_view()),
    #path('product-manager/update/<int:id>', views.UpdateProduct.as_view(), name='productUpdate'),
    #path('product-manager/create/category/',views.SetCategory.as_view()),
    #path('orders/', views.show_orders, name='sellerOrders'),
]