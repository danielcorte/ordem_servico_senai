from rest_framework import serializers
from .models import Gestores, Manutentores, Patrimonios, Ambientes, OrdemServico


class GestoresSerializers(serializers.Serializer):

    class Meta:
        model = Gestores
        fields = '__all__'

class ManutentoresSerializers(serializers.Serializer):

    class Meta:
        model = Manutentores
        fields = '__all__'

class PatrimoniosSerializers(serializers.Serializer):

    class Meta:
        model = Patrimonios
        fields = '__all__'

class AmbientesSerializers(serializers.Serializer):

    class Meta:
        model = Ambientes
        fields = '__all__'

class OrdemServicoSerializers(serializers.Serializer):

    class Meta:
        model = OrdemServico
        fields = '__all__'