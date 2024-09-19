from rest_framework import serializers

from .models import *
from .validators import *

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product_detail',lookup_field="pk")
    class Meta:
        model = Product
        fields = [
            'url',
            'id',
            #'user',
            'title',
            'content', 
            'price'
        ]
#    def create(self,validated_data):
 #       return Product.objects.create(**validated_data)



class FollowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Follow
        fields = [
            'follower',
            'following',
            'created_at'
        ]
        read_only_fields = ['follower', 'created_at']

    def validate(self,data):
        follower = self.context['request'].user
        following = data['following']

        if follower == following:
            raise serializers.ValidationError("You cannot follow yourself.")

        if Follow.objects.filter(follower=follower,following=following).exists():
            raise serializers.ValidationError("You are already following this user.")
            
        return data