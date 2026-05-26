from django import forms


INPUT_CLASS = (
    'w-full bg-surface-container-highest px-4 py-3 rounded-t-lg '
    'border-0 border-b-2 border-outline-variant/30 focus:border-primary '
    'focus:ring-0 text-on-surface font-body placeholder:text-on-surface-variant/40'
)


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'correo@ejemplo.com',
            'autocomplete': 'off',
            'class': INPUT_CLASS,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': INPUT_CLASS,
        })
    )


class RegistroForm(forms.Form):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej. Alejandro de la Vega',
            'class': INPUT_CLASS,
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'curador@biblioteca.org',
            'autocomplete': 'off',
            'class': INPUT_CLASS,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': INPUT_CLASS,
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': INPUT_CLASS,
        })
    )

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned


# Alias para compatibilidad
class PedidoForm(forms.Form):
    titulo = forms.CharField(max_length=255)
    autor  = forms.CharField(max_length=255)
    imagen = forms.URLField(required=False)
