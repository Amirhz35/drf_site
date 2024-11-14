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
from .tasks import *
from .getquery import *
from .mixins import PermissionMixins

'''
class FollowAPI(APIView):
    def get(self,request):
        queryset  = Follow.objects.all()
        serializer = FollowSerializer(queryset,many=True,context={"request":request})
        return Response(serializer.data)

    def post(self,request):
        serializer = FollowSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class FollowAPIView(
    GetFollowQuerySet,
    PermissionMixins,
    generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    def perform_create(self,serializer):
        serializer.save(follower=self.request.user)

class GetFollowersAPIView(
    PermissionMixins,
    generics.ListAPIView):
    serializer_class = FollowSerializer
    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)

class GetFollowingAPIView(
    PermissionMixins,
    generics.ListAPIView):
    serializer_class = FollowSerializer
    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
'''

class FollowAPIView(
    #GetFollowQuerySet,
    PermissionMixins,
    APIView):

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user) 

    def get(self,request):
        queryset = self.get_queryset()
        serializer = FollowSerializer(queryset,many=True)
        return Response(serializer.data,status=200)

    def post(self,request):
        serializer = FollowSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save(follower=self.request.user)
            return Response({"data":serializer.data},status=200)
        return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
follow_view = FollowAPIView.as_view()

class GetFollowersAPIView(
    PermissionMixins,
    APIView):
    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)

    def get(self,request):
        queryset = self.get_queryset()
        serializer = FollowSerializer(queryset,many=True)
        return Response(serializer.data)     
getfollowers = GetFollowersAPIView.as_view()

class GetFollowingAPIView(
    PermissionMixins,
    APIView):
    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
    def get(self,request):
        queryset = self.get_queryset()
        serializer = FollowSerializer(queryset,many=True)
        return Response(serializer.data)
getfollowing = GetFollowingAPIView.as_view()

class GetPostsAPIView(
    PermissionMixins,
    APIView):
    def get_queryset(self):
        following_user = Follow.objects.filter(follower=self.request.user).values_list('following', flat=True)
        return Product.objects.filter(user__in=following_user)

    def get(self,request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
getpost = GetPostsAPIView.as_view()

class SendEmailAPIView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient_list = request.data.get('recipient_list',[])
        send_email.delay(subject, message, recipient_list)
        return Response({'email has been sent successfully'},status=200)
send_email_view = SendEmailAPIView.as_view()

class UNFollowAPIView(APIView):
    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
    def get(self,request):
        queryset = self.get_queryset()
        serializers = FollowSerializer(queryset,many=True)
        return Response(serializers.data,status=200)
    def post(self,request):
        following_user_id = request.data.get('following')
        follower = request.user.id
        
        if not following_user_id:
            return Response({'error': 'Following user ID is required'}, status=400)
        
        if follower == following_user_id:
            return Response({'error': 'You cannot unfollow yourself'}, status=400)
        
        try:
            instance = Follow.objects.get(follower=request.user, following_id=following_user_id)
            instance.delete()
            return Response({'message': 'User unfollowed successfully'}, status=200)
        except Follow.DoesNotExist:
            return Response({'error': 'You are not following this user'}, status=400)


unfollow = UNFollowAPIView.as_view()