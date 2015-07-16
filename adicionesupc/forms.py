__author__ = 'EverL'
from django import forms
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
#from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Estudiante,Programa,Materia,Adicion

class FormularioPrograma(forms.ModelForm):
    class Meta:
        model= Programa
        fields = ['codigo','nombre']
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
        }


class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields = ['programa','codigo','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido']
        widgets={
            'programa':forms.Select(attrs={'class':'form-control'}),
            'codigo':forms.TextInput(attrs={'class':'form-control','placeholder':'digite codigo'}),
            'primer_nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'digite primer nombre'}),
            'segundo_nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'digite segundo nombre'}),
            'primer_apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'digite primer apellido'}),
            'segundo_apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'digite segundo apellido'}),

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
