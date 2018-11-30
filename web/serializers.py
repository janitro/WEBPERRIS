from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile,Contacto,Mascota



class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ('id','Nombre', 'Raza', 'Edad', 'Estado', 'Descripcion', 'Foto')