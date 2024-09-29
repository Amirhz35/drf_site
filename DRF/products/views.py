from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import *
from .serializers import *
from .getquery import *
from .mixins import PermissionMixins




class SomeThingsView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True,context={"request":request})
        return Response(serializer.data)
    def post(self,request):
        #queryset = request.data.get('queryset')
        serializer = ProductSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data})
        return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
something = SomeThingsView.as_view()


"""class FollowAPIView(APIView):
    def get(self,request):
        queryset  = Follow.objects.all()
        serializer = FollowSerializer(queryset,many=True,context={"request":request})
        return Response(serializer.data)

    def post(self,request):
        serializer = FollowSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)"""

class FollowAPIView(
    GetFollowQuerySet,
    PermissionMixins,
    generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    def perform_create(self,serializer):
        serializer.save(follower=self.request.user)
follow_view = FollowAPIView.as_view()


class GetFollowersAPIView(
    PermissionMixins,
    generics.ListAPIView):
    serializer_class = FollowSerializer
    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)
getfollowers = GetFollowersAPIView.as_view()

class GetFollowingAPIView(
    PermissionMixins,
    generics.ListAPIView):
    serializer_class = FollowSerializer
    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
getfollowing = GetFollowingAPIView.as_view()

class GetPostsAPIView(
    PermissionMixins,
    generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        following_user = Follow.objects.filter(follower=self.request.user).values_list('following', flat=True)
        return Product.objects.filter(user__in=following_user)
getpost = GetPostsAPIView.as_view()

class UNFollowAPIView(
    #GetFollowQuerySet,
    PermissionMixins,
    generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
    def perform_create(self,serializer):
        following_user  = self.request.data.get('following')

        try:
            instance = Follow.objects.get(follower=self.request.user,following_id=following_user)
            instance.delete()
            return Response({'user unfollowed successfully'},status=200)
        except Follow.DoesNotExist:
            return Response({'you are not following this user'})
    
unfollow = UNFollowAPIView.as_view()