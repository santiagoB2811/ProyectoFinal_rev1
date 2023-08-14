"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ProyectoFinal.views import saludo
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# LOGIN - REGISTRO - LOGOUT:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include ('App1.urls')), #Acá vinculo la ulr de App1 con la del proyecto
    path('AppLogin/', include ('AppLogin.urls')), #Acá vinculo la ulr de AppLogin con la del proyecto

]

# AVATARES:
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)