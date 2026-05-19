from django.contrib import admin
from .models import Gestor, Cliente

class GestorAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)

admin.site.register(Gestor, GestorAdmin)
admin.site.register(Cliente)