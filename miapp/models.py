from django.db import models
from django.contrib.auth.models import User


class Gestor(models.Model):
    usuario        = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento   = models.CharField(max_length=100)
    telefono       = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username


class Cliente(models.Model):
    usuario   = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono  = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.usuario.username


class Pedido(models.Model):
    ESTADOS = [
        ('pendiente',   'Pendiente'),
        ('preparacion', 'En preparación'),
        ('enviado',     'Enviado'),
        ('entregado',   'Entregado'),
        ('cancelado',   'Cancelado'),
    ]

    cliente     = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    titulo      = models.CharField(max_length=255, default='')
    autor       = models.CharField(max_length=255, default='')
    imagen      = models.URLField(blank=True, default='')
    descripcion = models.TextField(blank=True)
    estado      = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha       = models.DateTimeField(auto_now_add=True)
    precio      = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Pedido #{self.id} — {self.titulo} [{self.estado}]"

    @property
    def estado_icono(self):
        return {
            'pendiente':   'schedule',
            'preparacion': 'inventory_2',
            'enviado':     'local_shipping',
            'entregado':   'check_circle',
            'cancelado':   'cancel',
        }.get(self.estado, 'help')
