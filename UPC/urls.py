from django.conf.urls import include,url
from django.contrib import admin
from adicionesupc.views import *
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'UPC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^crearprograma/', CrearPrograma.as_view(), name='Crear'),

    url(r'^lista/', ListaPrograma.as_view(),name='lista'),

    url(r'^detalleprograma/(?P<pk>.*)$',DetallePrograma.as_view(), name='Detalle'),

    url(r'^eliminarprograma/(?P<pk>.*)$', EliminarPrograma.as_view(), name='eliminar'),

    url(r'^editarprograma/(?P<pk>.*)$',ActualizarPrograma.as_view(), name='actualizar'),

    url(r'^crearestudiante/', CrearEstudiante.as_view(), name='crearestudiante'),

    url(r'^index/', IndexView.as_view(), name='index'),

]
