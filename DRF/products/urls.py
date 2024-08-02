from django.urls import path
from products.views import *


urlpatterns = [
    path('',product_list_create),
    path('<int:pk>',product_detail,name='product_detail'),
    path('profile/<int:pk>',product_list_create)
]