from rest_framework import serializers
from .models import Gestores, Manutentores


class GestoresSerializers(serializers.Serializer):

    class Meta:
        model = Gestores
        fields = '__all__'

class ManutentoresSerializers(serializers.Serializer):

    class Meta:
        model = Manutentores
        fields = '__all__'