
from django.urls import path, re_path
from . import views

app_name ='home_app'

urlpatterns=[
	# primero url(si esta vacio, como en autores, entra al dominio principal 127.0.0.1:8000), luego vista a usar y luego un nombre 
	path('nuevoProyecto',views.AddProyecto.as_view() , name="add-proyecto"),
	#todo lo que este despues de url libros-autor/ hasta antes de otra / lo considere un pk y que recupere ese valor y lo guarde en ID
	path('user/<pk>',views.MostrarUser.as_view(), name="user-perfil"),

	path('proyectos',views.ListaProyecto.as_view(), name="lista-proyectos"),

	path('proyecto/<pk>',views.MostrarProyecto.as_view(), name="proyecto-perfil"),

	path('modify-user/<pk>',views.ModifyUser.as_view(), name="modify-user"),

	path('proyectos/<slug>',views.ProyectoCategoria.as_view(), name="proyecto-categoria"),


 ]