from itertools import product
from rest_framework import serializers
from .models import Product, Category, ProductCategory

class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(queryset=Product.objects.all(), many=True, slug_field='name')
    class Meta:
        model = Category
        fields = ('name', 'products')

class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(queryset=Category.objects.all(), many=True, slug_field='name')

    class Meta:
        model = Product
        fields = ('name', 'categories')

class PairsSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='name',read_only='True')
    category = serializers.SlugRelatedField(slug_field='name',read_only='True')
    class Meta:
        model = ProductCategory
        fields = ('product', 'category')