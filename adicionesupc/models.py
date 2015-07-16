from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Programa (models.Model):
    codigo = models.CharField(primary_key=True,max_length=20)
    nombre =  models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        #nombre en plural del modelo en el admin
        verbose_name_plural='Programas'


class Estudiante(models.Model):
    codigo = models.CharField(primary_key=True,max_length=12)
    programa = models.ForeignKey(Programa)
    primer_nombre= models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50,blank=True,null=True,default='No tiene')
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)

    #devuelve el nombre de la facultad en el admin
    def __str__(self):
        return self.primer_nombre

    class Meta:
        #nombre en plural del modelo en el admin
        verbose_name_plural='Estudiantes'


class Materia(models.Model):
    codigo = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

    class Meta:
        #nombre en plural del modelo en el admin
        verbose_name_plural='Materias'

class Adicion(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    materia = models.ForeignKey(Materia)
    grupo =  models.CharField(max_length=10)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.estudiante.primer_nombre,self.estudiante.codigo

    def adicionado_hoy(self):
        return self.fecha.date() == timezone.now().date()
    adicionado_hoy.boolean = True
    adicionado_hoy.short_description ='¿Adicionado hoy?'

    class Meta:
        #nombre en plural del modelo en el admin
        verbose_name_plural='Adiciones'
        ordering=['-fecha']


