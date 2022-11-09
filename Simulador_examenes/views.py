from gc import get_objects
from http import client
from multiprocessing import context
from multiprocessing.connection import Client
from sqlite3 import IntegrityError
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import Registrar_pregunta
from django.contrib.auth.decorators import login_required
from Simulador_examenes.models import pregunta


# Create your views here.

@login_required
def pagina_inicio(request):
    return render(request, 'inicio.html')


@login_required
def pamoid(request):
    return render(request, 'pamoid.html')


def registrarse(request):

    if request.method == 'GET':
        # Enviando la vista por la petición GET
        return render(request, 'registrarse.html',
                      {'form': UserCreationForm})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Creando el usuario
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],)

                user.save()
                login(request, user)
                return redirect(pagina_inicio)

            except IntegrityError:  # Error por duplicidad de datos únicos en la DB
                # Reenviando la vista por la petición GET
                return render(request, 'registrarse.html',
                              {'form': UserCreationForm,
                               'error': 'El usuario ya existe'})

        # Reenviando la vista por la petición GET
        return render(request, 'registrarse.html',
                      {'form': UserCreationForm,
                       'error': 'Las contraseñas no coinciden'})


@login_required
def pagina_principal_razonamiento(request):
    return render(request, 'pagina_principal_razonamiento.html')


@login_required
def series_numericas(request):
    return render(request, 'series_numericas.html')


def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html',
                      {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])

        if user is None:
            return render(request, 'iniciar_sesion.html',
                          {'form': AuthenticationForm,
                           'error': 'El usuario o contraseña no son correctos'})
        else:
            login(request, user)
            return redirect(pagina_inicio)


def cerrar_sesion(request):
    logout(request)
    return redirect(inicio_sesion)


@login_required
def registrar_pregunta(request):

    preguntas = pregunta.objects.all()

    if request.method == 'GET':
        # Enviando la vista por la petición GET
        return render(request, 'registrar_pregunta.html', {
            'form': Registrar_pregunta,
            'pregunta': preguntas
        })

    else:
        try:
            form = Registrar_pregunta(request.POST)
            nueva_pregunta = form.save(commit=False)
            nueva_pregunta.user = request.user
            nueva_pregunta.save()

            return render(request, 'registrar_pregunta.html',
                          {'form': Registrar_pregunta,
                           'pregunta': preguntas,
                           'correcto': 'Pregunta registrada correctamente'})

        except ValueError:
            return render(request, 'registrar_pregunta.html',
                          {'form': Registrar_pregunta,
                           'pregunta': preguntas,
                           'error': 'El registro no fue creado, por favor registra nuevamente'})


def pregunta_detalle(request, detalle_id):

    if request.method == 'GET':
        Pregunta = get_object_or_404(pregunta, pk=detalle_id)
        form = Registrar_pregunta(instance=Pregunta)

        return render(request, 'pregunta_detalle.html',
                      {
                          'pregunta': Pregunta,
                          'form': form
                      })

    else:
        try:
            Pregunta = get_object_or_404(pregunta, pk=detalle_id)
            form = Registrar_pregunta(request.POST, instance=Pregunta)
            form.save()

            return redirect(registrar_pregunta)

        except ValueError:
            return render(request, 'pregunta_detalle.html',
                          {
                              'pregunta': Pregunta,
                              'form': form,
                              'error': 'Error al actualizar el contenido'
                          })


def eliminar_pregunta(request, detalle_id):

    Pregunta = get_object_or_404(pregunta, pk=detalle_id)

    if request.method == 'POST':
        Pregunta.delete()
        return redirect(registrar_pregunta)  