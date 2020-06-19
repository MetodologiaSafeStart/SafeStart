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
	'foto_proyecto','foto_proyecto2',
	'nombre_usuario','rubro']
	success_url='/'

class ModifyUser(CreateView):
	template_name='home/modify-user.html'
	model= Usuario
	fields=['foto_perfil','profesion','presentacion','enlace_referencias']
	success_url='.'
	def get_queryset(self):
		id = self.kwargs['pk']
		lista=Usuario.objects.filter(
			id=id

			)
		return lista


class ListaProyecto(ListView):
	template_name='home/proyectos.html'
	model= Proyecto
	context_object_name='proyectos'
	paginate_by = 10
	

class MostrarUser(DetailView):
	template_name='home/user.html'
	model=Usuario
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
	model=Usuario

	def get_queryset(self):
		id = self.kwargs['pk']
		lista=Proyecto.objects.filter(
			id=id

			)
		return lista





