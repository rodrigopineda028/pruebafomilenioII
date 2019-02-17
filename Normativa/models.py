from django.db import models

class TipoNormativa(models.Model):
	descripcion = models.CharField('Tipo de normativa', max_length=200)

	def __str__(self):
		return self.descripcion

class Normativa(models.Model):
	nombre = models.CharField('Nombre', max_length=200, blank=False)
	normativa_gen = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Normativa generadora', blank=True, null=True)
	tipo_normativa = models.ForeignKey(TipoNormativa, on_delete=models.CASCADE, verbose_name='Tipo de normativa', blank=False, null=False)
	fecha_aprobacion = models.DateField('Fecha de aprobacion', blank=True, null=True)
	fecha_publicacion = models.DateField('Fecha de publicacion', blank=True, null=True)

	def __str__(self):
		return format(self.nombre)

class TipoInstitucion(models.Model):
	descripcion = models.CharField('Tipo de Institucion', max_length=200, blank=False, null=False)

	def __str__(self):
		return format(self.descripcion)

class Institucion(models.Model):
	nombre = models.CharField('Institucion', max_length=200, blank=False, null=False)
	tipo_institucion = models.ForeignKey(TipoInstitucion, on_delete=models.CASCADE, verbose_name='Tipo de institucion', blank=False, null=False)

	def __str__(self):
		return format(self.nombre)