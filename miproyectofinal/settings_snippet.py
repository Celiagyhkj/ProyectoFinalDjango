# ══════════════════════════════════════════════════════════════════
#  FRAGMENTO DE settings.py  — añade / modifica estas secciones
# ══════════════════════════════════════════════════════════════════

# 1. INSTALLED_APPS — añade estas apps si no las tienes:
INSTALLED_APPS = [
    # ... tus apps existentes ...
    'django.contrib.sites',       # ← necesario para allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # ← OAuth2 Google
    # tu app:
    'librizate',  # ← el nombre de tu app Django
]

# 2. SITE_ID (necesario para allauth)
SITE_ID = 1

# 3. AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',         # login normal
    'allauth.account.auth_backends.AuthenticationBackend', # OAuth2
]

# 4. Configuración de allauth
ACCOUNT_EMAIL_VERIFICATION  = 'none'      # no requiere verificar email
ACCOUNT_LOGIN_ON_GET        = True
LOGIN_REDIRECT_URL          = '/inicio/'  # tras login exitoso
LOGOUT_REDIRECT_URL         = '/'         # tras logout

# 5. Proveedor Google (Client ID y Secret los obtienes en Google Cloud Console)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id':     'TU_GOOGLE_CLIENT_ID_AQUI',
            'secret':        'TU_GOOGLE_CLIENT_SECRET_AQUI',
            'key':           '',
        }
    }
}

# 6. MIDDLEWARE — asegúrate de tener (allauth lo necesita):
MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # ...
]

# ══════════════════════════════════════════════════════════════════
#  COMANDOS PARA ACTIVAR TODO
# ══════════════════════════════════════════════════════════════════
#
#  pip install django-allauth openpyxl requests
#
#  python manage.py makemigrations
#  python manage.py migrate
#  python manage.py createsuperuser
#
#  Luego en /admin/ → Sites → cambia "example.com" por "localhost:8000"
#  Y en Social Applications → añade Google con tu Client ID y Secret
#
# ══════════════════════════════════════════════════════════════════
