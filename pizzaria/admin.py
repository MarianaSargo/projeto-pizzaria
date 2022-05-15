from django.contrib import admin
from .models import Restaurante, Encomenda, Cliente, Menu


# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Cliente)
admin.site.register(Menu)
admin.site.register(Encomenda)
