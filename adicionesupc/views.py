from django.shortcuts import render_to_response
from .models import Estudiante,Programa,Materia,Adicion
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView,TemplateView
from .forms import FormularioEstudiante,FormularioPrograma,FormularioMateria,FormularioAdicion
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,authenticate
from  django.template import RequestContext

#login

class IndexView(TemplateView):
    template_name = "index.html"
#-----------Programa--------------

class CrearPrograma(CreateView):
    model = Programa
    template_name ='createviewprograma.html'
    form_class = FormularioPrograma
    success_url = "/"


class ListaPrograma(ListView):
    template_name = 'listviewprograma.html'
    model = Programa

class DetallePrograma(DetailView):
    template_name = 'detailviewprograma.html'
    model = Programa


class EliminarPrograma(DeleteView):
    template_name = 'deleteviewprograma.html'
    model=Programa
    success_url = "/"


class ActualizarPrograma(UpdateView):
    template_name = 'updateviewprograma.html'
    model=Programa
    form_class = FormularioPrograma
    success_url = "/"

#--------------Estudiante---------------

class CrearEstudiante(CreateView):
    model = Estudiante
    template_name = 'createviewestudiante.html'
    form_class = FormularioEstudiante
    success_url = reverse_lazy('lista')


class ListaEstudiante(ListView):
    template_name = 'listviewestudiante.html'
    model = Estudiante


class DetalleEstudiante(DetailView):
    template_name = 'detailviewestudiante.html'
    model = Estudiante


class EliminarEstudiante(DeleteView):
    template_name = 'deleteviewestudiante.html'
    model=Estudiante
    success_url = "/"


class ActualizarEstudiante(UpdateView):
    template_name = 'updateviewestudiante.html'
    model=Estudiante
    form_class = FormularioEstudiante
    success_url = "/"


#-----------Materia--------------

class CrearMateria(CreateView):
    model = Materia
    template_name = 'createview.html'
    form_class = FormularioMateria
    success_url = "/"

#listar todos los programas
class ListaMateria(ListView):
    template_name = 'listview.html'
    model = Materia

#detalle de un programa
class DetalleMateria(DetailView):
    template_name = 'detailview.html'
    model = Materia

#eliminar un programa
class EliminarMateria(DeleteView):
    template_name = 'deleteview.html'
    model=Materia
    success_url = "/"

#actualizar un modelo
class ActualizarMateria(UpdateView):
    template_name = 'updateview.html'
    model=Materia
    form_class = FormularioMateria
    success_url = "/"


#-----------Adicion--------------

class CrearAdicion(CreateView):
    model = Adicion
    template_name = 'createview.html'
    form_class = FormularioAdicion
    success_url = "/"

#listar todos los programas
class ListaAdicion(ListView):
    template_name = 'listview.html'
    model = Adicion

#detalle de un programa
class DetalleAdicion(DetailView):
    template_name = 'detailview.html'
    model = Adicion

#eliminar un programa
class EliminarAdicion(DeleteView):
    template_name = 'deleteview.html'
    model=Adicion
    success_url = "/"

#actualizar un modelo
class ActualizarAdicion(UpdateView):
    template_name = 'updateview.html'
    model=Adicion
    form_class = FormularioAdicion
    success_url = "/"
