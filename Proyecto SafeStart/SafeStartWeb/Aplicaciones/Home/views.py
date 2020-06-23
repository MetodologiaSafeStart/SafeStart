from django.shortcuts import render
from django.views.generic import(ListView,
	CreateView, DetailView,TemplateView
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

class ProyectoCategoria(ListView):
	template_name='home/proyecto-categoria.html'

	context_object_name = 'proyectos'

	def get_queryset(self):

		rubro = self.kwargs['slug']
		lista=Proyecto.objects.filter(
			rubro=rubro

			)
		
		return lista

class BaseView(TemplateView):
	template_name = 'home/base.html'

class IndexView(TemplateView):
	template_name = 'home/index.html'

class ComoFunciona(TemplateView):
	template_name = 'home/como-funciona.html'

class Nosotros(TemplateView):
	template_name = 'home/nosotros.html'

class Contacto(TemplateView):
	template_name = 'home/contacto.html'

class Categorias(TemplateView):
	template_name = 'home/categorias.html'










