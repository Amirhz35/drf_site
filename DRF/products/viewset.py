from rest_framework import viewsets

from .models import *
from .serializers import *
from .getquery import *
from .mixins import PermissionMixins

class ProductViewSet(
    GetProductQuerySet,
    PermissionMixins,
    viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)


DetailViewSet = ProductViewSet.as_view({'get': 'retrieve','put': 'update',
    'patch': 'partial_update','delete': 'destroy'})
ListAndCreateViewSet = ProductViewSet.as_view({'get':'list', 'post':'create'})

