from django.urls import path
from products.views import *
from .viewset import *


urlpatterns = [
    path('<int:pk>',DetailViewSet,name='product_detail'),
    path('profile',ListAndCreatrViewSet),
    path('follow',follow_view),
    path('some',something),
    path('followers',getfollowers),
    path('following',getfollowing),
    path('posts',getpost),
    path('unfollow',unfollow)
]