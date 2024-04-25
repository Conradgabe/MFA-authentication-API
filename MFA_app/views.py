from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import BlockUnverifiedEmail

class Register(APIView):
    serializer_class = CustomUserSerializer

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class Users(APIView):
    permission_classes = [BlockUnverifiedEmail]

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        list_users = [user.email for user in users]

        return Response(list_users, status=status.HTTP_200_OK)