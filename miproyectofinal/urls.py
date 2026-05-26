from django.urls import path, include
from miapp import views

urlpatterns = [
    # ── Páginas generales ──
    path('',               views.inicio_sin_sesion, name='inicio_sin_sesion'),
    path('inicio/',        views.inicio,            name='inicio'),
    path('catalogo/',      views.catalogo,          name='catalogo'),
    path('perfil/',        views.perfil,            name='perfil'),
    path('gestor/',        views.gestor,            name='gestor'),

    # ── Autenticación propia ──
    path('inicio_sesion/', views.inicio_sesion,     name='inicio_sesion'),
    path('registro/',      views.registro,          name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),

    # ── OAuth2 Google (django-allauth) ──
    path('accounts/',      include('allauth.urls')),

    # ── Pedidos ──
    path('crear_pedido/',                          views.crear_pedido,          name='crear_pedido'),
    path('pedidos/',                               views.mis_pedidos,           name='mis_pedidos'),
    path('pedidos/<int:pedido_id>/estado/',        views.cambiar_estado_pedido, name='cambiar_estado_pedido'),
    path('pedidos/<int:pedido_id>/cancelar/',      views.cancelar_pedido,       name='cancelar_pedido'),
    path('pedidos/<int:pedido_id>/pdf/',           views.exportar_pdf,          name='exportar_pdf'),
    path('pedidos/exportar/excel/',                views.exportar_excel,        name='exportar_excel'),

    # ── Legacy ──
    path('add_carrito/',   views.add_carrito,       name='add_carrito'),
    path('pedido/',        views.detalle_pedido,    name='detalle_pedido'),
]
