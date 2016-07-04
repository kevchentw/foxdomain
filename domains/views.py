from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .permissions import IsOwner
from .permissions import IsAdminOrReadOnly
from .serializers import DomainSerializer
from .models import Domain
from .serializers import SubDomainSerializer
from .models import SubDomain

class DomainList(generics.ListAPIView):
    """
    A view to list all domain.
    Permission: Public
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = (AllowAny,)


class DomainCreate(generics.CreateAPIView):
    """
    A view to create domain.
    Permission: Admin
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = (IsAdminUser,)


class SubDomainCreate(generics.CreateAPIView):
    """
    A view to create subdomain.
    Permission: Authenticated User
    """
    queryset = SubDomain.objects.all()
    serializer_class = SubDomainSerializer
    permission_classes = (IsAuthenticated,)
