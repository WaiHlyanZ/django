from django.contrib.auth.models import User
from rest_framework import serializers

# In this case, serializer convert python objects to JSON vice-versa
# JSON is the standard format for communicating web apps

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # `wirte_only` ensure that the password is only used when creating or updating a user and is never exposed in API responses
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        @parameter 
        `validated_data`: checked from above Meta class done by django
        @return
        a new user
        """
        user = User.objects.create_user(**validated_data)
        return user