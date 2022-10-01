"""Plataforma_educativa_policial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from Simulador_examenes import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.pagina_inicio),
    path('pamoid/', views.pamoid),
    path('pamoid/razonamiento/', views.pagina_principal_razonamiento),
    path('pamoid/razonamiento/series/', views.series_numericas),
    path('registrarse/', views.registrarse),
    path('iniciar_sesion/', views.inicio_sesion),
    path('cerrar_sesion/', views.cerrar_sesion),
    path('registrar_pregunta/', views.registrar_pregunta),
    path('registrar_pregunta/<int:detalle_id>/', views.pregunta_detalle, name= 'detalle_pregunta'),
    path('registrar_pregunta/<int:detalle_id>/eliminar', views.eliminar_pregunta, name= 'eliminar_pregunta'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
