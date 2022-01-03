from django.urls import path
from .views import create_connection , list_connection , create_user , list_user , \
    crypto , crypto_list , create_crypto , create_number , editdelete_number , create_price , price , kavenegar
from rest_framework import routers
from . import views

urlpatterns = [

    path("create_connection/" , create_connection.as_view() , name = "create_connection"),
    path("list_connection/" , list_connection.as_view() , name = "list_connection"),
    path("create_user/" , create_user.as_view() , name = "create_user"),
    path("list_user/" , list_user.as_view() , name = "list_user"),
    path("crypto_list/" , crypto_list.as_view() , name = "crypto_list"),
    path("crypto/<int:pk>/" , crypto.as_view() , name = "crypto"),
    path("create_crypto/" , create_crypto.as_view() , name = "create_crypto"),
    path("create_number/" , create_number.as_view() , name = "create_number"),
    path("number/" , editdelete_number.as_view() , name = "number"),
    path("create_price/" , create_price.as_view() , name = "create_price"),
    path("price/<int:pk>/" , price.as_view() , name = "price"),
    path("kavenegar/<int:pk>/" , kavenegar.as_view() , name = "kavenegar"),

]


