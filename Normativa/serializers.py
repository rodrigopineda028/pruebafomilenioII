from rest_framework import serializers
from .models import Normativa, TipoNormativa, Institucion, TipoInstitucion

class NormativaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Normativa
		fields = ('__all__')

class TipoNormativaSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoNormativa
		fields = ('__all__')

class InstitucionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Institucion
		fields = ('__all__')

class TipoInstitucionSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoInstitucion
		fields = ('__all__')