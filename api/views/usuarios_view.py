from rest_framework import generics
from ..models import Usuario
from ..serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout feito com sucesso."})


class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer