from django.db import models

# Create your models here.
class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nome}'

class Menu(models.Model):
    pizza = models.CharField(max_length=100)
    bebida = models.CharField(max_length=100)
    NomeRestaurante = models.ManyToManyField(Restaurante)
    def __str__(self):
        return f'Pizza: {self.pizza} com {self.bebida}'

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    def __str__(self):
        return f'{self.name} ({self.age})'

class Encomenda(models.Model):

    NomeCliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name = 'cliente'
        )

    NomeMenu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name = 'menu'
        )
    hora = models.DateTimeField()


    def __str__(self):
        return f'Encomenda: {self.pk} de {self.NomeCliente} com {self.NomeMenu} à hora:{self.hora}'




