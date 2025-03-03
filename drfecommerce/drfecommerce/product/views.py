from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer

# Create your views here.
class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
 
