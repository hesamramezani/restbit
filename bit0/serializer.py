from rest_framework import serializers
from .models import connection_model, choise, crypto_model
from django.contrib.auth.models import User
from rest_framework import fields


class connection_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = connection_model
        fields = "__all__"


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class crypto_serializer(serializers.ModelSerializer):
    field = fields.MultipleChoiceField(choices=choise)
    class Meta:
        model = crypto_model
        fields = "__all__"


