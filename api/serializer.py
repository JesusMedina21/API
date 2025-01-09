from rest_framework import serializers
from .models import instrumento


class InstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = instrumento
        # fields = ('fullname', 'nickname')
        fields = '__all__'
