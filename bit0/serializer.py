from rest_framework import serializers
from .models import connection_model
from django.contrib.auth.models import User

class connection_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = connection_model
        fields = "__all__"


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
