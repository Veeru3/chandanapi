from rest_framework import viewsets
from .Productserializer import ProductSerializer
from .models import Product
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer