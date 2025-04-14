from rest_framework import serializers
from .models import Gestores, Manutentores, Patrimonios, Ambientes, OrdemServico

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'nivel']

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'nivel']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "As senhas não coincidem"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    



class GestoresSerializers(serializers.ModelSerializer):

    class Meta:
        model = Gestores
        fields = '__all__'
    

class ManutentoresSerializers(serializers.ModelSerializer):

    class Meta:
        model = Manutentores
        fields = '__all__'

class PatrimoniosSerializers(serializers.ModelSerializer):

    class Meta:
        model = Patrimonios
        fields = '__all__'

class AmbientesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ambientes
        fields = '__all__'

class OrdemServicoSerializers(serializers.ModelSerializer):

    class Meta:
        model = OrdemServico
        fields = '__all__'