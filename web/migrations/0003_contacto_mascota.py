# Generated by Django 2.1.3 on 2018-11-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20181116_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=50)),
                ('Comentario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Raza', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Estado', models.CharField(choices=[('Diposible', 'Disponible'), ('Rescatado', 'Rescatado'), ('Adoptado', 'Adoptado')], max_length=20)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Foto', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]