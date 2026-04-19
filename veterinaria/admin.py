from django.contrib import admin
from .models import Cliente, Mascota, Consulta

admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Consulta)