from django.urls import path
from .views import create_connection , list_connection

urlpatterns = [

    path("create_connection/" , create_connection.as_view() , name = "create_connection"),
    path("list_connection/" , list_connection.as_view() , name = "list_connection"),


]


