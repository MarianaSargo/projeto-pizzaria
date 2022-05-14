from django.contrib import admin
from .models import Restaurante, encomenda, pessoa, entrega


# Register your models here.
admin.site.register(Restaurante)
admin.site.register(encomenda)
admin.site.register(pessoa)
admin.site.register(entrega)