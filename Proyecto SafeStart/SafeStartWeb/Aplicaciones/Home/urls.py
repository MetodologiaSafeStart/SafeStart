from django.urls import path, re_path
from . import views

app_name ='home_app'

urlpatterns=[
	
	path('',views.IndexView.as_view(), name="index"),

	path('categorias',views.Categorias.as_view(), name="categorias"),

	path('registrate',views.SignUpView.as_view(), name="sign_up"),

	path('como-funciona',views.ComoFunciona.as_view(), name="como-funciona"),

	path('nosotros',views.Nosotros.as_view(), name="nosotros"),

	path('contacto',views.Contacto.as_view(), name="contacto"),

	path('nuevoProyecto',views.AddProyecto.as_view() , name="add-proyecto"),
	
	path('user/<pk>',views.MostrarUser.as_view(), name="user-perfil"),

	path('proyectos',views.ListaProyecto.as_view(), name="lista-proyectos"),

	path('proyecto/<pk>',views.MostrarProyecto.as_view(), name="proyecto-perfil"),

	path('modify-user/<pk>',views.ModifyUser.as_view(), name="modify-user"),

	path('proyectos/<slug>',views.ProyectoCategoria.as_view(), name="proyecto-categoria"),

	path('iniciar-sesion/', views.SignInView.as_view(), name='sign_in'),
	
	path('cerrar-sesion/', views.SignOutView.as_view(), name='sign_out'),
	
	path('perfil/<slug>',views.AddPerfil.as_view(), name='perfil'),


	path('proyectos-autor/<slug>',views.ProyectoUser.as_view(), name='proyectos-autor'),



	


 ]