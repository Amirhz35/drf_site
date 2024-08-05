from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product_detail',lookup_field="pk")
    class Meta:
        model = Product
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content', 
            'price'
        ]


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = [
            'follower',
            'followeing',
            'created_at'
        ]