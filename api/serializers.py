from rest_framework import serializers
from .models import Gestores, Manutentores, Patrimonios, Ambientes, OrdemServico, Usuario

from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'role')
    
    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
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