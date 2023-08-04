from django.shortcuts import render
from django.http import HttpResponse
from App1.forms import UserRegisterForm, User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from App1.forms import AseguradoraFormulario, ProductorFormulario, UserRegisterForm, UserEditForm, AvatarFormulario
from AppLogin.models import Avatar

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'inicio.html', {'url':avatares[0].imagen.url})


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppLogin/inicioLogueado.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppLogin/inicioLogueado.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppLogin/inicioLogueado.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppLogin/login.html", {"form": form})

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppLogin/inicioRegistrado.html" ,  {"mensaje":"Usuario creado correctamente."})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppLogin/registro.html" ,  {"form":form})

# EDICION DE USUARIO:
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password2 = informacion['password2']
            usuario.password1 = informacion['password1']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            
            usuario.save()
            
            return render(request, "inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppLogin/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

# AVATAR:
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, "inicio.html")
    else:
        miFormulario=AvatarFormulario()
        
    return render(request, "AppLogin/agregarAvatar.html", {'miFormulario': miFormulario})