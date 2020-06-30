from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import(ListView,
	CreateView, DetailView,TemplateView
	)
# Create your views here.

from .models import Usuario, Proyecto
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView 

class AddProyecto(CreateView):
	template_name='home/add-proyecto.html'
	model= Proyecto
	second_model=Usuario
	fields=['nombre_proyecto','descripcion_proyecto',
	'foto_proyecto','foto_proyecto2',
	'nombre_usuario','rubro']
	success_url='/'

class ModifyUser(CreateView):
	template_name='home/modify-user.html'
	model= Usuario
	fields=['fecha_nacimiento','foto_perfil','profesion','presentacion','enlace_referencias']
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

class Login(TemplateView):
	template_name = 'home/perfil_form.html'

class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm
	

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=user, password=password)
        login(self.request, user)
        return redirect('home/modify-user')


class SignInView(LoginView):
    template_name = 'home/iniciar_sesion.html'


class SignOutView(LogoutView):
    pass


class AddPerfil(CreateView):
	template_name='home/perfil.html'
	model= Usuario
	fields=['fecha_nacimiento','foto_perfil','profesion','presentacion','enlace_referencias']
	success_url='/'