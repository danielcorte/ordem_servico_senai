from rest_framework import serializers
from .models import Gestores


class GestoresSerializers(serializers.Serializer):

    class Meta:
        model = Gestores
        fields = '__all__'
