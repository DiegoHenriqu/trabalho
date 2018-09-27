from django.db import models
from django.utils import timezone

class Farmacia(models.Model) :
     nomeFarmacia = models.CharField(max_length=50)
     nomeCliente = models.CharField(max_length=50)
     nomeFuncionario = models.CharField(max_length=50)
     laboratorio = models.CharField(max_length=50)
     nomeRemedio = models.CharField(max_length=50)

     def __str__(self):
         return self.nomeFarmacia




