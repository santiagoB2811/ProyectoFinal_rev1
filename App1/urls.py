from django.urls import path
from App1 import views
from .views import *


urlpatterns = [
    path('', views.inicio, name = 'Inicio'), #esta va a ser la primera vista. SIEMPRE LA PRIMER LETRA VA A IR EN MAYUSCULA
    path('coberturas', views.coberturas, name = 'Coberturas'),
    path('aseguradoras', views.aseguradoras, name = 'Aseguradoras'),
    path('productores', views.productores, name = 'Productores'),   
    #path('aseguradoraFormulario', views.aseguradoraFormulario, name = 'AseguradoraFormulario'),
    #path('productorFormulario', views.productorFormulario, name = "ProductorFormulario"),
    path('busquedaAseguradora', views.busquedaAseguradora, name='BusquedaAseguradora'),
    path('buscar', views.buscar),
    path('busquedaCobertura', views.busquedaCobertura, name='BusquedaCobertura'),
    path('busquedaProductor', views.busquedaProductor, name = 'BusquedaProductor'),
    
# CRUD para coberturas:
    path("coberturas/list", CoberturasList.as_view(), name = "coberturas_list"),
    path('coberturas/<pk>', CoberturasDetalle.as_view(), name = 'coberturas_detalle'),
    path('coberturas/nuevo/', CoberturasCreacion.as_view(), name = 'coberturas_crear'),
    path('coberturas/editar/<pk>', CoberturasUpdate.as_view(), name = 'coberturas_editar'),
    path('coberturas/borrar/<pk>', CoberturasDelete.as_view(), name = 'coberturas_borrar'),
# CRUD para aseguradoras:
    path("aseguradoras/list", AseguradorasList.as_view(), name = "aseguradoras_list"),
    path('aseguradoras/<pk>', AseguradorasDetalle.as_view(), name = 'aseguradoras_detalle'),
    path('aseguradoras/nuevo/', AseguradorasCreacion.as_view(), name = 'aseguradoras_crear'),
    path('aseguradoras/editar/<pk>', AseguradorasUpdate.as_view(), name = 'aseguradoras_editar'),
    path('aseguradoras/borrar/<pk>', AseguradorasDelete.as_view(), name = 'aseguradoras_borrar'),
# CRUD para productores:
    path("productores/list", ProductoresList.as_view(), name = "productores_list"),
    path('productores/<pk>', ProductoresDetalle.as_view(), name = 'productores_detalle'),
    path('productores/nuevo/', ProductoresCreacion.as_view(), name = 'productores_crear'),
    path('productores/editar/<pk>', ProductoresUpdate.as_view(), name = 'productores_editar'),
    path('productores/borrar/<pk>', ProductoresDelete.as_view(), name = 'productores_borrar'),
# ABOUT US:
    path('aboutUs', views.about_us, name = 'AboutUs'),

    ]
