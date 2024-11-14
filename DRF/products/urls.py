from django.urls import path
from products.views import *
from .viewset import *


urlpatterns = [
    path('<int:pk>',DetailViewSet,name='product_detail'),
    path('profile',ListAndCreateViewSet),
    path('follow',follow_view),
    path('followers',getfollowers),
    path('following',getfollowing),
    path('posts',getpost),
    path('unfollow',unfollow),
    path('email',send_email_view)
]