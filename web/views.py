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


@api_view(['GET', 'POST'])
def perro_lista(request,):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        mascota = Mascota.objects.all()
        serializer = MascotaSerializer(mascota, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def perro_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MascotaSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MascotaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




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



"""def MascotaReg(request):
    
    if request.method == 'POST':
        form = MascotasForm(request.POST, request.FILES)
        if form.is_valid():
           mascota = form.save(commit=False)
           mascota.username = request.user
           mascota.save()
           messages.success(request, 'Mascota Agregada')
           return redirect('home')
    else:
       form = MascotasForm()
       
        
    
    return render(request, 'mascotas.html', {'form': form})"""

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


# def Perros_list(request):
#     posts = Mascota.objects.all()
#     return render(request, 'mascotasListar.html', {'posts': posts})



# class MascotaViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Mascota.objects.all()
#     serializer_class = MascotaSerializer




def ListarPerros(request):
    response = requests.get('http://127.0.0.1:8000/Listado/')
    if response.status_code == 200:
        listaperros = response.json()
        results = listaperros.get('results', [])
      
        return render(request, 'mascotasListar.html', {
            'results': results,
      
        
        })

        
 

               
       
         
   



# class MascotaDatail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'mascota3.html'

#     def get(self, request, pk):
#         mascota = get_object_or_404(Mascota, pk=pk)
#         serializer = MascotaSerializer(mascota)
#         return Response({'serializer': serializer, 'mascota': mascota})

#     def post(self, request, pk):
#         mascota = get_object_or_404(Mascota, pk=pk)
#         serializer = MascotaSerializer(mascota, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'mascota': mascota})
#         serializer.save()
#         return redirect('home')

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

class MascotaList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name =    'mascota3.html'

    def get(self, request):
        queryset = Mascota.objects.all()
        return Response({'listamascota': queryset})





