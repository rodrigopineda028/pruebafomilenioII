from django.conf.urls import url, include
from .views import NormativasApiView, TipoNormativaApiView, InstitucionApiView, TipoInstApiView

urlpatterns = [
	url(r'^api/normativa/$', NormativasApiView.as_view()),
	url(r'^api/tiponormativa/', TipoNormativaApiView.as_view()),
	url(r'^api/institucion/', InstitucionApiView.as_view()),
	url(r'^api/tipoinstitucion/', TipoInstApiView.as_view())
]