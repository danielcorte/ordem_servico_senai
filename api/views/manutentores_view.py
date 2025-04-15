from django.shortcuts import render

from ..models import Manutentores
from ..serializers import ManutentoresSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class ManutentoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Manutentores.objects.all()
    serializer_class = ManutentoresSerializers
    permission_classes = [IsAuthenticated]

class ManutentoresListCreateView(ListCreateAPIView):
    queryset = Manutentores.objects.all()
    serializer_class = ManutentoresSerializers
    permission_classes = [IsAuthenticated]

class ManutentoresSearchView(ListAPIView):
    queryset = Manutentores.objects.all()
    serializer_class = ManutentoresSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_filters = ['ni', 'nome', 'area', 'gestor']

