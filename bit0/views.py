from rest_framework.generics import CreateAPIView , ListAPIView
from .models import connection_model
from .serializer import connection_model_serializer , user_serializer
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

class create_connection(CreateAPIView):
    queryset = connection_model.objects.all()
    serializer_class = connection_model_serializer

class list_connection(ListAPIView):
    queryset = connection_model.objects.all()
    serializer_class = connection_model_serializer
    permission_classes = (IsAdminUser ,)

class create_user(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer

class list_user(ListAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer


