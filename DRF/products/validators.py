from .serializers import *
from rest_framework.serializers import Serializer

 

def uniqe_follower(value):
    qs = Follow.objects.filter(followeing__exact=value)
    if qs.exists():
        raise serializers.ValidationError("must be a new follower")
    return value