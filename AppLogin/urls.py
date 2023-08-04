from django.urls import path
from AppLogin import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', views.inicio, name = 'Inicio'), #esta va a ser la primera vista. SIEMPRE LA PRIMER LETRA VA A IR EN MAYUSCULA
    path('login', views.login_request,name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='Applogin/logout.html'), name='Logout'),
    # EDICION DE USUARIO:
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    # AGREGAR AVATAR:
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
]
     