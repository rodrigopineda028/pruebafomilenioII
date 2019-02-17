from django.contrib import admin

from .models import TipoNormativa
from .models import Normativa
from .models import TipoInstitucion
from .models import Institucion

admin.site.register(TipoNormativa)
#admin.site.register(Normativa)
admin.site.register(TipoInstitucion)
admin.site.register(Institucion)

#Se vuelve a registrar para personalizar campos mostrados en admin
@admin.register(Normativa)
class Normativa(admin.ModelAdmin):
	list_display=('nombre', 'tipo_normativa', 'fecha_aprobacion', 'fecha_publicacion', 'normativa_gen')