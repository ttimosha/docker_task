from django.urls import path
from django.contrib import admin
from .views import ProductAPIView, CategoryAPIView, PairsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', ProductAPIView.as_view()),
    path('categories', CategoryAPIView.as_view()),
    path('pairs', PairsAPIView.as_view()),
]