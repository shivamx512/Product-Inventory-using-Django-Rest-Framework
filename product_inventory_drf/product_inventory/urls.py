from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product_inventory import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'product_categories', views.ProdcutCategoryViewSet, basename='product_categories')


urlpatterns = [
    path('', include(router.urls)),
]