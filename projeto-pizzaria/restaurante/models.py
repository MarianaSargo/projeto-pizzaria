from django.db import models

# Create your models here.
class Restaurante(models.Model):
    comidas = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.comidas}'


class encomenda(models.Model):

    food = models.ForeignKey(
        Restaurante,
        on_delete=models.CASCADE,
        related_name = 'pizza'
        )

    drink = models.ForeignKey(
        Restaurante,
        on_delete=models.CASCADE,
        related_name = 'bebida'
        )

    def __str__(self):
        return f'Encomenda: {self.pk} da {self.food} com {self.drink}'


class pessoa(models.Model):
    name = models.CharField(max_length=50)
    Encomenda = models.ManyToManyField(encomenda)

    def __str__(self):
        return f'{self.name}'

class entrega(models.Model):
    local = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.local}'