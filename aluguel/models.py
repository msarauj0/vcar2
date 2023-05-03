from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    
    cpf = models.CharField("CPF",max_length=15, primary_key=True)
    nome = models.CharField("Nome",max_length=250)
    telefone = models.CharField("Telefone",max_length=50)
    data_nascimento = models.DateField("Data de Nascimento")
    endereco = models.CharField("Endereço",max_length=150)

    def __str__(self):
        return "{}".format(self.nome)

class Car(models.Model):

    placa = models.CharField("Placa", max_length=100)
    marca = models.CharField("Marca", max_length=100)
    modelo = models.CharField("Modelo", max_length=100)
    ano = models.CharField("Ano",max_length=7)
    data_comprar = models.DateField("Data de compra")

    def __str__(self):
        return "{} - {}".format(self.marca, self.modelo)


class Aluguel(models.Model):

    codigo = models.CharField("Codigo", max_length=100)
    data_aluguel = models.DateField("Data de aluguel")
    data_devolucao = models.DateField("Data de devolução")
    diaria = models.DecimalField("Diaria",max_digits=10, decimal_places=2)

    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.cliente.nome, self.carro.modelo)