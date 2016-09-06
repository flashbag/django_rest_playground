from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics

from rest_framework import status
from rest_framework import mixins

from rest_framework import viewsets

from rest_framework import permissions

from management.models import User
from management.serializers import UserSerializer
from management.permissions import IsOwnerOrReadOnly


class UserList(generics.ListCreateAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer

	permission_classes = (permissions.IsAdminUser,)


class UserDetail(generics.RetrieveAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer