from rest_framework import viewsets

from product_inventory.models import Product, ProductCategory
from product_inventory.serializers import ProductSerializer, ProductCategorySerializer
from product_inventory.custom_pagination import ProductPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        """
        override get_queryset for db query optimization, 
        here we used select related to fetch category data in single query.
        """
        return Product.objects.select_related(
            "category",
        )

class ProdcutCategoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = ProductPagination