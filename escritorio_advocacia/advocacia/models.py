# advocacia/models.py

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='processos')
    nome = models.CharField(max_length=255)
    numero = models.CharField(max_length=50)
    data_abertura = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.numero}"