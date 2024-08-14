
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# A view to create a new user
class CreateUserView(generics.CreateAPIView): # generics.CreateAPIView handles creating a new user or object
    # Looking for all objects in User when create a new user and ensure is a new user
    querset = User.objects.all()
    # To accept valid data (username, password)
    serializer_class = User
    # Allowed anyone to use this view
    permission_classes = [AllowAny]