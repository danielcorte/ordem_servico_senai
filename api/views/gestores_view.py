from django.shortcuts import render

from ..models import Gestores
from ..serializers import GestoresSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class GestoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Gestores.objects.all()
    serializer_class = GestoresSerializers
    permission_classes = [IsAuthenticated]

class GestoresListCreateView(ListCreateAPIView):
    queryset = Gestores.objects.all()
    serializer_class = GestoresSerializers
    permission_classes = [IsAuthenticated]

class GestoresSearchView(ListAPIView):
    queryset = Gestores.objects.all()
    serializer_class = GestoresSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_filters = ['ni', 'nome', 'area', 'cargo']

