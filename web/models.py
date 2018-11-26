from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField('Rut',max_length=12,null=True)
    fecha_nacimiento = models.DateField('Fecha Nacimiento',null=True)
    region = models.CharField('Region',max_length=50,null=True)
    ciudad = models.CharField('Ciudad',max_length=50,null=True)
    tipo_vivienda = models.CharField('Tipo de Vivienda',max_length=50,null=True)

    def __str__(self):
     return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class Mascota(models.Model):
    ES_MASCOTA =  (
        ('Diposible', 'Disponible'),
        ('Rescatado', 'Rescatado'),
        ('Adoptado', 'Adoptado'),
    )
    Nombre = models.CharField(max_length=50)
    Raza = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Estado = models.CharField(max_length=20,
    choices=ES_MASCOTA)
    Descripcion =  models.CharField(max_length=100)
    Foto = models.ImageField(upload_to='Perros', null=True, blank=True)


    def __str__(self):
     return self.Nombre



class Contacto(models.Model):
    Nombre= models.CharField(max_length=50)
    Correo = models.EmailField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Comentario = models.CharField(max_length=200)

    def __str__(self):
     return self.Nombre















    



