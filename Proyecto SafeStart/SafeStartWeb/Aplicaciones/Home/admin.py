from django.contrib import admin
from .models import Usuario, Proyecto

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		'fecha_nacimiento',
		'foto_perfil',
		'profesion',
		'correo',
		'presentacion',
		'enlace_referencias'
		)

	search_fields =('nombre', 'profesion',)

class ProyectoAdmin(admin.ModelAdmin):
	list_display = (
		'nombre_proyecto',
		'descripcion_proyecto',
		'foto_proyecto',
		'foto_proyecto2',
		'fecha_publicacion',
		'nombre_usuario',
		'rubro'
		)

	list_filter=('fecha_publicacion',
		'rubro',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Proyecto, ProyectoAdmin)