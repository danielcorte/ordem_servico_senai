from django.shortcuts import render

from ..models import Patrimonios
from ..serializers import PatrimoniosSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class PatrimoniosDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Patrimonios.objects.all()
    serializer_class = PatrimoniosSerializers
    permission_classes = [IsAuthenticated]

class PatrimoniosListCreateView(ListCreateAPIView):
    queryset = Patrimonios.objects.all()
    serializer_class = PatrimoniosSerializers
    permission_classes = [IsAuthenticated]

class PatrimoniosSearchView(ListAPIView):
    queryset = Patrimonios.objects.all()
    serializer_class = PatrimoniosSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_filters = ['ni', 'descricao', 'localizao']

