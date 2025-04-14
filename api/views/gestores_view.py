from django.shortcuts import render

from ..models import Gestores
from ..serializers import GestoresSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def listar_gestores(request):
    if request.method == 'GET':
        queryset = Gestores.objects.all()
        serializer = GestoresSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = GestoresSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

