from distutils.command.upload import upload
from email.mime import image
from django.db import models


# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cidade_natal = models.CharField(max_length=200)
    foto_perfil = models.ImageField(upload_to='media', blank=True, null=True)
    def __str__(self):
        return self.nome