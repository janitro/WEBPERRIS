from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from web.models import Mascota,Contacto

class SignUpForm(UserCreationForm):
    run = forms.CharField(max_length=12)
    fecha_nacimiento = forms.DateField()
    region = forms.CharField(max_length=50)
    ciudad = forms.CharField(max_length=50)
    tipo_vivienda = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'run', 'email', 'first_name', 'password1', 'password2', 'fecha_nacimiento', 'region', 
        'ciudad', 'tipo_vivienda', )



class MascotasForm(forms.ModelForm):
    Nombre = forms.CharField(widget=forms.TextInput
    (attrs={'class':'form-control'}))
    Raza = forms.CharField(widget=forms.TextInput
    (attrs={'class':'form-control'}))
    Edad = forms.IntegerField(widget=forms.NumberInput
    (attrs={'class':'form-control'}))
    
    Descripcion = forms.CharField(widget=forms.TextInput
    (attrs={'class':'form-control'}))
   



    class Meta:
        model = Mascota
        fields = ('Nombre', 'Raza', 'Edad', 'Estado', 'Descripcion', 'Foto', )



class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ('Nombre', 'Correo', 'Telefono', 'Comentario', )

  