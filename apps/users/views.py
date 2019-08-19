from django.shortcuts import render

# Create your views here.
from apps.users.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }