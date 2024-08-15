from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Alumnos(models.Model): #define la estructura de nuetra tabla.
    matricula = models.CharField(max_length=12,verbose_name="Matricula") #texto corto
    nombre = models.TextField() #texto largo
    carrera = models.TextField(null=True)
    turno = models.CharField(max_length=10)
    edad = models.IntegerField(null=True)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    created= models.DateField(auto_now_add=True, verbose_name="fecha creación") #fecha y tiempo
    updated=models.DateField(auto_now_add=True, verbose_name="fecha modificación")

    class Meta:
        verbose_name= "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
        #el menos indica que se ordena del más reciente al mas viejo
        #str manejo de cadena

    def __str__(self):
        return self.nombre
        #indica que se mostrára el nombre como valor en la tabla 

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="clave")
    alumno = models.ForeignKey(Alumnos,on_delete=models.CASCADE,verbose_name="Alumno")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment=RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name= "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
    def __str__(self):
        return self.coment
    

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje =models.TextField( verbose_name="Comentario")
    created = models.DateTimeField( auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name= "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.mensaje


