from rest_framework.routers import DefaultRouter

from products.viewset import *

router = DefaultRouter()
router.register('products',ProductViewSet,basename='products')
urlpatterns = router.urls