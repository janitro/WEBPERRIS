from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from web.forms import SignUpForm, MascotasForm,ContactoForm
from web.models import Mascota,Contacto
from django.contrib import messages



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


def Perros_list(request):
    posts = Mascota.objects.all()
    return render(request, 'mascotasListar.html', {'posts': posts})