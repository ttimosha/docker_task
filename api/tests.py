from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Product, Category, ProductCategory
from .serializers import ProductSerializer, CategorySerializer, PairsSerializer

class SetUpBaseTest(APITestCase):
    client = APIClient()

    def setUp(self):
        dota = Product.objects.create(name = 'dota2')
        witcher = Product.objects.create(name = 'witcher')
        games = Category.objects.create(name='games')
        books = Category.objects.create(name='books')
        ProductCategory.objects.create(product = dota, category = games)
        ProductCategory.objects.create(product = witcher, category = games)
        ProductCategory.objects.create(product = witcher, category = books)

        Product.objects.create(name = 'apple')
        Category.objects.create(name = 'apple')

class GetAllPairsTest(SetUpBaseTest):
    
    def test_all_pairs(self):
        responce = self.client.get(reverse('pairs'))

        expected = PairsSerializer(ProductCategory.objects.all(), many=True)

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.data, expected.data)

class GetAllProductsTest(SetUpBaseTest):
    
    def test_all_pairs(self):
        responce = self.client.get(reverse('products'))

        expected = ProductSerializer(Product.objects.all(), many=True)

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.data, expected.data)

class GetAllPCategoriesTest(SetUpBaseTest):
    
    def test_all_pairs(self):
        responce = self.client.get(reverse('categories'))

        expected = CategorySerializer(Category.objects.all(), many=True)

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.data, expected.data)