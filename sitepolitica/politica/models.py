from django.db import models
from django.utils import timezone

class Cadastro(models.Model) :
        nomecandidato = models.CharField(max_length=50)
        tipodecandidatura = models.CharField(max_length=50)
        partido = models.CharField(max_length=50)
        cidadecandidato = models.CharField(max_length=50)
        coligacao = models.CharField(max_length=50)



