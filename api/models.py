from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 250)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 250)
    products = models.ManyToManyField(
        Product,
        through = 'ProductCategory',
        related_name = 'categories'
    )
    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.product.name}, {self.category.name}'