from django import forms
from django.core import validators

# REGISTRO
class RegistroForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        min_length=2,
        label="Nombre completo"
    )

    email = forms.EmailField(label="Correo electrónico")

    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=4,
        label="Contraseña"
    )


# LOGIN
class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña"
    )


# PEDIDOS
class PedidoForm(forms.Form):
    descripcion = forms.CharField(
        widget=forms.Textarea,
        label="Descripción del pedido",
        min_length=5
    )