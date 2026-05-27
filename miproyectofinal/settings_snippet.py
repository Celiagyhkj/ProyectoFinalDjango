INSTALLED_APPS = [
    'django.contrib.sites',       
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', 
    'librizate',  
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',         
    'allauth.account.auth_backends.AuthenticationBackend', 
]

ACCOUNT_EMAIL_VERIFICATION  = 'none'      
ACCOUNT_LOGIN_ON_GET        = True
LOGIN_REDIRECT_URL          = '/inicio/'  
LOGOUT_REDIRECT_URL         = '/'         

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

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',   
]