from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import NormativaSerializer, TipoNormativaSerializer, InstitucionSerializer, TipoInstitucionSerializer

from Normativa import services
from .models import Normativa, Institucion, TipoNormativa, TipoInstitucion

def home_view(request, *args, **kwargs):
	normativaFilter = request.GET.get('nombre', '')
	normativas_list = {
		'items': services.getNormativas(normativaFilter)
		}
	return render(request, 'home.html', normativas_list)


################
##	  API    ###
################

class NormativasApiView(generics.ListAPIView):
	queryset = Normativa.objects.all()
	serializer_class = NormativaSerializer

	#Para filtrar por nombre
	def get_queryset(self):
		filter = self.request.query_params.get('nombre', '')
		return Normativa.objects.filter(nombre__contains=filter)

class TipoNormativaApiView(generics.ListAPIView):
	queryset = TipoNormativa.objects.all()
	serializer_class = TipoNormativaSerializer

class InstitucionApiView(generics.ListAPIView):
	queryset = Institucion.objects.all()
	serializer_class = InstitucionSerializer

class TipoInstApiView(generics.ListAPIView):
	queryset = TipoInstitucion.objects.all()
	serializer_class = TipoInstitucionSerializer

