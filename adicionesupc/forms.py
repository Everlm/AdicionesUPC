__author__ = 'EverL'
from django import forms
from .models import Estudiante,Programa,Materia,Adicion,Facultad



class FormularioPrograma(forms.ModelForm):
    class Meta:
        model= Programa
        fields = ['codigo','nombre']
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control','required':True}),
            'nombre':forms.TextInput(attrs={'class':'form-control','required':True}),
        }

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields = ['programa','codigo','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','correo']
        widgets={
            'programa':forms.Select(attrs={'class':'form-control','required':True}),
            'codigo':forms.TextInput(attrs={'class':'form-control','required':True,'placeholder':'Identificacion'}),
            'primer_nombre':forms.TextInput(attrs={'class':'form-control','required':True,'placeholder':'Primer nombre'}),
            'segundo_nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo nombre'}),
            'primer_apellido':forms.TextInput(attrs={'class':'form-control','required':True,'placeholder':' Primer apellido'}),
            'segundo_apellido':forms.TextInput(attrs={'class':'form-control','required':True,'placeholder':'Segundo apellido'}),
            'correo':forms.EmailInput(attrs={'class':'form-control','required':True,'placeholder':'Email'}),


        }

class FormularioMateria(forms.ModelForm):
    class Meta:
        model= Materia
        fields = ['codigo','nombre']
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control','placeholder':'digite codigo'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'digite nombre'}),

        }

class FormularioAdicion(forms.ModelForm):
    class Meta:
        model= Adicion
        fields = ['estudiante','materia','grupo']
        widgets={
            'estudiante':forms.TextInput(attrs={'class':'form-control','placeholder':'elija estudiante'}),
            'materia':forms.TextInput(attrs={'class':'form-control','placeholder':'digite materia'}),
            'grupo':forms.TextInput(attrs={'class':'form-control','placeholder':'digite grupo'}),

        }

