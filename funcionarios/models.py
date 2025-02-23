from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    sexo = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.nome
