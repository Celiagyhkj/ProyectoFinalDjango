"""
repositories.py — Patrón Repository (punto 7 del proyecto)
Separa completamente el acceso a datos de las vistas.
"""
from .models import Pedido, Cliente
from django.contrib.auth.models import User


class ClienteRepository:

    @staticmethod
    def get_or_create(user):
        cliente, _ = Cliente.objects.get_or_create(usuario=user)
        return cliente

    @staticmethod
    def get_by_user(user):
        return Cliente.objects.filter(usuario=user).first()


class PedidoRepository:

    @staticmethod
    def get_all_by_cliente(cliente):
        return Pedido.objects.filter(cliente=cliente).order_by('-fecha')

    @staticmethod
    def get_by_id(pedido_id, cliente):
        return Pedido.objects.filter(pk=pedido_id, cliente=cliente).first()

    @staticmethod
    def filtrar_por_estado(cliente, estado=''):
        qs = Pedido.objects.filter(cliente=cliente)
        if estado:
            qs = qs.filter(estado=estado)
        return qs.order_by('-fecha')

    @staticmethod
    def crear(cliente, titulo, autor, imagen='', precio=0, descripcion=''):
        return Pedido.objects.create(
            cliente=cliente,
            titulo=titulo,
            autor=autor,
            imagen=imagen,
            precio=precio,
            descripcion=descripcion,
            estado='pendiente',
        )

    @staticmethod
    def cambiar_estado(pedido, nuevo_estado):
        estados_validos = [e[0] for e in Pedido.ESTADOS]
        if nuevo_estado not in estados_validos:
            raise ValueError(f"Estado inválido: {nuevo_estado}")
        pedido.estado = nuevo_estado
        pedido.save()
        return pedido

    @staticmethod
    def cancelar(pedido):
        if pedido.estado in ['cancelado', 'entregado']:
            raise ValueError("No se puede cancelar este pedido.")
        pedido.estado = 'cancelado'
        pedido.save()
        return pedido

    @staticmethod
    def contadores(cliente):
        todos = Pedido.objects.filter(cliente=cliente)
        return {
            'todos':       todos.count(),
            'pendiente':   todos.filter(estado='pendiente').count(),
            'preparacion': todos.filter(estado='preparacion').count(),
            'enviado':     todos.filter(estado='enviado').count(),
            'entregado':   todos.filter(estado='entregado').count(),
            'cancelado':   todos.filter(estado='cancelado').count(),
        }

    @staticmethod
    def get_todos_para_excel():
        return Pedido.objects.select_related('cliente__usuario').order_by('-fecha')


class UsuarioRepository:

    @staticmethod
    def crear(email, password, full_name=''):
        if User.objects.filter(username=email).exists():
            raise ValueError("El email ya está registrado.")
        user = User.objects.create_user(username=email, email=email, password=password)
        if full_name:
            partes = full_name.strip().split(' ', 1)
            user.first_name = partes[0]
            user.last_name  = partes[1] if len(partes) > 1 else ''
            user.save()
        Cliente.objects.create(usuario=user)
        return user
