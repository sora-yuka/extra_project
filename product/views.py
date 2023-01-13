from django.shortcuts import render
from product.models import Product, Category
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger('product')


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


#? Пример мидлвейра 
# @api_view(['GET'])
# def get_example(request):
    # print(request.hello)
    # return Response("Example")