from rest_framework import generics
from .models import Product, Category, ProductCategory
from .serializers import ProductSerializer, CategorySerializer, PairsSerializer

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PairsAPIView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = PairsSerializer