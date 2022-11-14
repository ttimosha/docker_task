from django.urls import path
from django.contrib import admin
from .views import ProductAPIView, CategoryAPIView, PairsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', ProductAPIView.as_view(), name = 'products'),
    path('categories', CategoryAPIView.as_view(), name = 'categories'),
    path('pairs', PairsAPIView.as_view(), name = 'pairs'),
]