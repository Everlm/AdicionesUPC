from django.contrib import admin
from adicionesupc.models import Estudiante,Materia,Programa,Adicion,Facultad

class AdicionAdmin(admin.ModelAdmin):
    list_display = ('estudiante','materia','fecha','adicionado_hoy')
    list_filter = ['fecha']
    search_fields = ['estudiante']


admin.site.register(Adicion,AdicionAdmin)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('codigo','programa','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','correo')
    list_filter = ['programa']
    search_fields = ['codigo','primer_nombre','segundo_apellido']

admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Materia)
admin.site.register(Programa)
admin.site.register(Facultad)


