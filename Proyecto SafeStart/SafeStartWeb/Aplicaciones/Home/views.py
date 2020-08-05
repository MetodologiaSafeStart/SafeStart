from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import(ListView,
	CreateView, DetailView,TemplateView
	)
# Create your views here.

from .models import Usuario, Proyecto
from .forms import SignUpForm, Perfil
from django.contrib.auth.views import LoginView, LogoutView 

class AddProyecto(CreateView):
	template_name='home/add-proyecto.html'
	model= Proyecto
	fields=['nombre_proyecto','descripcion_proyecto',
	'foto_proyecto','foto_proyecto2',
	'nombre_usuario','rubro']
	success_url='/'

	def form_valid(self, form):
		self.object= form.save(commit=False)
		self.object.user= self.request.user
		return super(AddProyecto, self).form_valid(form)


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

class ProyectoUser(ListView):
	template_name='home/proyecto-user.html'

	context_object_name = 'proyectos'

	def get_queryset(self):

		username = self.kwargs['slug']
		lista=Proyecto.objects.filter(
			nombre_usuario__username=username

			)
		
		return lista

class BaseView(TemplateView):
	template_name = 'home/base.html'

class IndexView(TemplateView):
	template_name = 'home/index.html'

	model=Usuario


	model= Usuario


class ComoFunciona(TemplateView):
	template_name = 'home/como-funciona.html'

class Nosotros(TemplateView):
	template_name = 'home/nosotros.html'

class Contacto(TemplateView):
	template_name = 'home/contacto.html'

class Categorias(TemplateView):
	template_name = 'home/categorias.html'

class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm
	

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        user = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=user, password=password)
        login(self.request,user)
        return redirect('/')


class SignInView(LoginView):
    template_name = 'home/iniciar_sesion.html'


class SignOutView(LogoutView):
    pass

#def AddPerfil(request, pk):
	#post = get_object_or_404(Usuario, pk=pk)
	#if request.method == "POST":
		#form = Perfil(request.POST, instance=post)
		#if form.is_valid():
			#post = form.save(commit=False)
			#post.user = request.user
			#post.save()
			#return redirect('/')
	#else:
		#form = Perfil(instance=post)
	#return render(request, 'home/perfil.html', {'form': form})

class AddPerfil(CreateView):
	template_name='home/perfil.html'
	model= Usuario
	form_class=Perfil
	#form=AddPerfil(initial={'user':id_user})
	success_url='/'

	def form_valid(self, form):
		self.object= form.save(commit=False)
		self.object.user= self.request.user
		return super(AddPerfil, self).form_valid(form)

	
    