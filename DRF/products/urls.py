from django.urls import path
from products.views import *


urlpatterns = [
    path('',productview),
    path('<int:pk>',product_detail,name='product_detail'),
    path('profile',product_list_create),
    path('follow/<int:pk>',follow_view)
]