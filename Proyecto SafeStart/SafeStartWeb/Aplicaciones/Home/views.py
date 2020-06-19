from django.shortcuts import render
from django.views.generic import(ListView,
	CreateView, DetailView,
	)
# Create your views here.

from .models import Usuario, Proyecto

class AddProyecto(CreateView):
	template_name='home/add-proyecto.html'
	model= Proyecto
	second_model=Usuario
	nombre_usuario= Usuario.nombre
	fields=['nombre_proyecto','descripcion_proyecto',
	'foto_proyecto','foto_proyecto2','fecha_publicacion',
	'nombre_usuario','rubro']
	success_url='/'

class ModifyUser(CreateView):
	template_name='home/modify-user.html'
	model= Usuario
	fields=['foto_perfil','profesion','presentacion','enlace_referencias']
	success_url='.'


class ListaProyecto(ListView):
	template_name='home/proyectos.html'
	model= Proyecto
	context_object_name='proyectos'
	paginate_by = 10
	def get_queryset(self):
		queryset = super(ListaProyecto, self).get_queryset()
		fecha = date.today()
		if self.request.GET.get('fecha'):
			from datetime import datetime
			fecha_str = self.request.GET.get('fecha')
			fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
		return queryset.filter(fecha_publicacion =fecha)

class MostrarUser(DetailView):
	template_name='home/user.html'
	context_object_name='user'

	def get_queryset(self):
		id = self.kwargs['pk']
		lista=Usuario.objects.filter(
			id=id

			)
		return lista

class MostrarProyecto(DetailView):
	template_name='home/proyecto.html'
	context_object_name='proyecto'
	

	def get_queryset(self):	
		id = self.kwargs['pk']
		lista=Proyecto.objects.filter(
				id=id
			)
		return lista





