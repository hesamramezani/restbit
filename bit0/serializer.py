from rest_framework import serializers
from .models import connection_model

class connection_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = connection_model
        fields = "__all__"


