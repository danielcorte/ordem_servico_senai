from rest_framework import generics, permissions
from ..serializers import RegistroSerializer, UsuarioSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]

class UsuarioView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user