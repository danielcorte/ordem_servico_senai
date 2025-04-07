from django.shortcuts import render

from ..models import Ambientes
from ..serializers import AmbientesSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class AmbientesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializers
    permission_classes = [IsAuthenticated]

class AmbientesListCreateView(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializers
    permission_classes = [IsAuthenticated]

class AmbientesSearchView(ListAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_filters = ['ni', 'nome', 'responsavel']

