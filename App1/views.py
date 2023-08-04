from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Aseguradoras, Productores, Coberturas
from App1.forms import AseguradoraFormulario, ProductorFormulario, UserRegisterForm, UserEditForm#, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #permitira que los objetos se carguen por detras (en background) para que el acceso sea mas rapido
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio (request):
   return render(request,'inicio.html')

def coberturas (request):
    return render(request,'coberturas.html')

#def aseguradoras(request):
 #   return render(request,'aseguradoras.html')

def productores(request):
    return render(request,'productores.html')

def aseguradoras(request):
    if request.method == 'POST': #preguntamos si es un metodo POST:
        miFormulario = AseguradoraFormulario(request.POST) # Aqui me llega la informacion del html (generamos los datos para el POST)
        print(miFormulario) 

        if miFormulario.is_valid(): #tomamos los valores
            informacion = miFormulario.cleaned_data
            aseguradora = Aseguradoras(nombre=informacion['nombre'],
                                        direccion=informacion['direccion'], 
                                        email=informacion['email'],
                                        telefono=informacion['telefono'])  #generamos el objeto
            aseguradora.save() #lo guardamos
            return render(request, 'inicio.html') #volvemos al inicio
    else:
        miFormulario = AseguradoraFormulario() #sino, generamos el objeto
           
    return render(request, 'aseguradoras.html', {"miFormulario": miFormulario}) #acá le mando los datos al formulario como un .

def productores(request):
    if request.method == 'POST': #preguntamos si es un metodo POST:
        miFormulario = ProductorFormulario(request.POST) # Aqui me llega la informacion del html (generamos los datos para el POST)
        print(miFormulario) 

        if miFormulario.is_valid(): #tomamos los valores
            informacion = miFormulario.cleaned_data
            productor = Productores(nombre=informacion['nombre'],
                                    apellido=informacion['apellido'], 
                                    email=informacion['email'],
                                    telefono=informacion['telefono'])  #generamos el objeto
            productor.save() #lo guardamos
            return render(request, 'inicio.html') #volvemos al inicio
    else:
        miFormulario = ProductorFormulario() #sino, generamos el objeto
           
    return render(request, 'productores.html', {"miFormulario": miFormulario}) #acá le mando los datos al formulario

def busquedaAseguradora(request):
    return render (request, 'busquedaAseguradora.html')  

def buscar(request):
    # Comento lo que utilizamos anteriormente:
    # respuesta = f"Estoy buscando la camada Nro: {request.GET['camada']}"

    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        aseguradoras = Aseguradoras.objects.filter(nombre_icontains=nombre)

        return render (request, 'resultadosPorBusqueda.html', {'nombre': nombre})  
    
    else:
        respuesta = 'No enviaste datos.'
    
    return HttpResponse(respuesta)
    #return render(request, 'resultadosPorBusqueda.html', {"respuesta": respuesta})

def busquedaCobertura(request):
    return render (request, 'busquedaCobertura.html')  

def busquedaProductor(request):
    return render (request, 'busquedaProductor.html')  


#hago CRUD para las coberturas:

class CoberturasList(ListView):
    model = Coberturas
    template_name = 'coberturas_2.html'

class CoberturasDetalle(DetailView):
    model = Coberturas
    template_name = 'coberturas_detalle.html'


class CoberturasCreacion(CreateView):
    model = Coberturas
    template_name = 'crearCobertura.html'
    success_url= reverse_lazy("coberturas_list")
    fields = '__all__'

class CoberturasUpdate(UpdateView):
    model =  Coberturas
    success_url = reverse_lazy('coberturas_editar')
    template_name = 'coberturas_form.html'
    fields = ['nombre', 'ramo']

class CoberturasDelete(DeleteView):
    model =  Coberturas
    template_name = 'coberturas_confirm_delete.html'
    success_url = reverse_lazy("coberturas_list")

# Hago CRUD para las aseguradoras:
class AseguradorasList(ListView):
    model = Aseguradoras
    template_name = 'aseguradoras_2.html'

class AseguradorasDetalle(DetailView):
    model = Aseguradoras
    template_name = 'aseguradoras_detalle.html'

class AseguradorasCreacion(CreateView):
    model = Aseguradoras
    template_name = 'crearAseguradora.html'
    success_url= reverse_lazy("aseguradoras_list")
    fields = '__all__'

class AseguradorasUpdate(UpdateView):
    model = Aseguradoras
    success_url = reverse_lazy('aseguradoras_editar')
    template_name = 'aseguradoras_form.html'
    fields = ['nombre', 'direccion', 'email', 'telefono']

class AseguradorasDelete(DeleteView):
    model = Aseguradoras
    template_name = 'aseguradoras_confirm_delete.html'
    success_url = reverse_lazy("aseguradoras_list")

# Hago CRUD para los productores:

class ProductoresList(ListView):
    model = Productores
    template_name = 'productores_2.html'

class ProductoresDetalle(DetailView):
    model = Productores
    template_name = 'productores_detalle.html'

class ProductoresCreacion(CreateView):
    model = Productores
    template_name = 'crearProductor.html'
    success_url= reverse_lazy("productores_list")
    fields = '__all__'

class ProductoresUpdate(UpdateView):
    model = Productores
    success_url = reverse_lazy('productores_editar')
    template_name = 'productores_form.html'
    fields = ['nombre', 'apellido', 'email', 'telefono']

class ProductoresDelete(DeleteView):
    model = Productores
    template_name = 'productores_confirm_delete.html'
    success_url = reverse_lazy("productores_list")

# ABOUT US:
def about_us(request):
    return render(request,'aboutUs.html')

