from django.urls import path
from . import views



router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')



urlpatterns = [
    path(' ', include(router.urls)),
    path('profile/', views.seller_profile,name='sellerProfile'),
    path('product-manager/', views.ProductManager.as_view(), name="productManager"),
    path('product-manager/create/', views.CreateProduct.as_view()),
    path('product-manager/update/<int:id>', views.UpdateProduct.as_view(), name='productUpdate'),
    path('product-manager/create/category/',views.SetCategory.as_view()),
    path('orders/', views.show_orders, name='sellerOrders'),
]