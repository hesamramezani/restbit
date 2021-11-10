from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , ListAPIView
from .models import connection_model , crypto_model
from .serializer import connection_model_serializer , user_serializer , crypto_serializer
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .permission import IsSuperUser
from rest_framework.response import Response


class create_connection(CreateAPIView):
    queryset = connection_model.objects.all()
    serializer_class = connection_model_serializer

class list_connection(ListAPIView):
    queryset = connection_model.objects.all()
    serializer_class = connection_model_serializer
    permission_classes = (IsAdminUser,)

class create_user(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer

class list_user(ListAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer
    permission_classes = (IsSuperUser,)


class select_crypto(CreateAPIView):
    queryset = crypto_model.objects.all()
    serializer_class = crypto_serializer


class crypto_list(ListAPIView):
    queryset = crypto_model.objects.all()
    serializer_class = crypto_serializer

