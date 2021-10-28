from django.urls import path
from .views import create_connection , list_connection , create_user , list_user

urlpatterns = [

    path("create_connection/" , create_connection.as_view() , name = "create_connection"),
    path("list_connection/" , list_connection.as_view() , name = "list_connection"),
    path("create_user/" , create_user.as_view() , name = "create_user"),
    path("list_user/" , list_user.as_view() , name = "list_user"),

]


