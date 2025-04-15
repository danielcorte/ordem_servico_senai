from django.shortcuts import render

from ..models import OrdemServico
from ..serializers import OrdemServicoSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class OrdemServicoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializers
    permission_classes = [IsAuthenticated]

class OrdemServicoListCreateView(ListCreateAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializers
    permission_classes = [IsAuthenticated]

class OrdemServicoSearchView(ListAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_filters = ['descricao', 'abertura', 'fechamento', 
                      'status', 'patrimonio', 'ambiente', 
                      'manutentor', 'responsavel', 'prioridade']

