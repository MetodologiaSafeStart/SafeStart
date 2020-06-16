from django.db import models
class Usuario(models.Model):#TABLA DE LA BASE DE DATOS
    nombre= models.CharField('Nombre',max_length=25,help_text='Ingrese su nombre')
    fecha_nacimiento=models.DateField(help_text='Fecha de nacimiento')
    foto_perfil=models.ImageField(help_text='Elije una foto',null=True,blank=True)
    profesion=models.CharField(help_text='Profesión',max_length=30,null=True,blank=True)
    correo=models.EmailField(help_text='Ingrese su correo')
    presentacion=models.TextField(help_text='Acerca de ti',max_length=200,null=True,blank=True)
    enlace_referencias=models.CharField(help_text='Link',max_length=50,null=True,blank=True)

    def __str__(self):

        return self.nombre


class Proyecto(models.Model):
   
    RUBRO_CHOICES = (
       ('AO', 'Administración/Oficina'),
       ('AL', 'Almacén'),
       ('AC', 'Atención a clientes'),
       ('CT', 'CallCenter/Telemercadeo'),
       ('CE', 'Comercio Exterior'),
       ('CP', 'Compras'),
       ('CC', 'Comunicación'),
       ('CO', 'Construccion y obra'),
       ('CF', 'Contabilidad/Finanzas'),
       ('DG','Dirección/Gerencia'),
       ('DA','Diseño/Artes gráficas'),
       ('DC','Docencia'),
       ('HO','Hostelería'),
       ('IN','Informática'),
       ('IG','Ingeniería'),
       ('IC','Investigación y Calidad'),
       ('LA','Legal, Asesoría'),
       ('LO','Logística'),
       ('MR','Mantenimiento y Reparaciones Técnicas'),
       ('MF','Manufactura'),
       ('MS','Medicina/Salud'),
       ('MT','Mercadotécnia') ,
       ('OP','Operarios'),
       ('OT','Otros'),
       ('PR','Producción') ,
       ('PU','Publicidad'),
       ('RH','Recursos Humanos'),
       ('SG','Servicios Generales'),
       ('SE','Seguridad'),
       ('TC','Telecomunicaciones'),
       ('TR','Transporte'),
       ('TU','Turismo'),
       ('VE','Ventas'),
      )

    nombre_proyecto= models.CharField('Nombre',max_length=25,help_text='Ingrese el nombre del proyecto')
    descripcion_proyecto=models.TextField(help_text='Acerca del Proyecto',max_length=200)
    foto_proyecto=models.ImageField(help_text='Elije una foto',null=True,blank=True)
    foto_proyecto2=models.ImageField(help_text='Elije una foto',null=True,blank=True)
    fecha_publicacion=models.DateField(help_text='Fecha de publicacion',auto_now_add=True)
    nombre_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    rubro=models.CharField(max_length=25,help_text='Seleccione el rubro',choices=RUBRO_CHOICES)

  
    def __str__(self):
        return self.nombre_proyecto




    



    
    

