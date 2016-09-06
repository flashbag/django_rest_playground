from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics

from rest_framework import status
from rest_framework import mixins

from rest_framework import viewsets

from management.models import User
from management.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides `list` and `detail` actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer