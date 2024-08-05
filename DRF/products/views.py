from django.shortcuts import render
from rest_framework import generics

from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *
from .getquery import GetQuerySet
from .mixins import PermissionMixins
# Create your views here.

class ProductListCreateView(
    GetQuerySet,
    PermissionMixins,
    generics.ListCreateAPIView,
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_list_create = ProductListCreateView.as_view()


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
product_detail = ProductDetailView.as_view()


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
productview = ProductView.as_view()


class FollowView(generics.RetrieveAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    lookup_field = 'pk'
    def follow(self,serializer):
        user_to_follow = get_object_or_404(User,id = lookup_field)
        if not self.request.user.following.filter(id=lookup_field).exists():
            Follow.objects.create(follower=self.request.user,followeing=user_to_follow)  
                 

follow_view = FollowView.as_view()