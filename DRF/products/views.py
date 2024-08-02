from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
from .getquery import GetQuerySet
# Create your views here.

class ProductListCreateView(
    generics.ListCreateAPIView,
    GetQuerySet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

product_list_create = ProductListCreateView.as_view()


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
product_detail = ProductDetailView.as_view()