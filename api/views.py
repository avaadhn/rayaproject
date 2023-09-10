from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import Category, Product
from api.serializers import ProductSerializer ,CategorySerializer

class MostSell(APIView):
    def get(self, request):
        products = Product.objects.all().order_by('-selled_count')
        answer = ProductSerializer(products, many=True)
        return Response(answer.data)


class Specials(APIView):
    def get(self, request):
        products = Product.objects.filter(special=True)
        answer = ProductSerializer(products, many=True)
        return Response(answer.data)


class Categories(APIView):
    def get(self, request):
        Categories = Category.objects.all()
        answer = CategorySerializer(Categories, many=True)
        return Response(answer.data)
    

class Product(APIView):
    def get(self, request):
        Category = request.GET.get("category", 0)
        name = request.GET.get("name", "")
        products = Product.objects.all()
        if Category:
            products = Product.filter(category__id=Category)
        if name:
            products = Product.filter(name__contains=name)
        answer = ProductSerializer(products, many=True)
        return Response(answer.data)

# Create your views here.
