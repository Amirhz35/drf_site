from django.urls import path
from products.views import *


urlpatterns = [
    path('',productview),
    path('<int:pk>',product_detail,name='product_detail'),
    path('profile',product_list_create),
    path('follow',follow_view),
    path('some',something),
    path('followers',getfollowers),
    path('following',getfollowing),
    path('posts',getpost)
]