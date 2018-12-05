from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from web.forms import SignUpForm, MascotasForm,ContactoForm
from web.models import Mascota,Contacto
from django.contrib import messages
from .serializers import MascotaSerializer
from rest_framework import viewsets, generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import requests
from rest_framework.decorators import api_view


def home(request):
    
    return render(request,"home.html")


def login(request):
    
    return render(request,"login.html") 






def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.run = form.cleaned_data.get('run')
            user.profile.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            user.profile.region  = form.cleaned_data.get('region')
            user.profile.ciudad  = form.cleaned_data.get('ciudad')
            user.profile.tipo_vivienda  = form.cleaned_data.get('tipo_vivienda')
            user.save()
            messages.success(request, 'Usuario Agregado')
           
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def MascotaReg(request):
    if request.method == 'POST':
        form = MascotasForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
          
           
            return redirect('home')
    else:
        form = MascotasForm()
    return render(request, 'mascotas.html', {
        'form': form
    })


def ContactoReg(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
          
           
            return redirect('home')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {
        'form': form
    })



def ListarPerros(request):
    response = requests.get('http://127.0.0.1:8000/Listado')
    if response.status_code == 200:
        listaperros = response.json()
        results = listaperros.get('results', [])
      
        return render(request, 'mascotasListar.html', {
            'results': results,
      
        
        })










def Prueba(request):
    
    return render(request,"prueba2.html") 




        
 

               
         
   





class Listado (generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class ListadoDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer







