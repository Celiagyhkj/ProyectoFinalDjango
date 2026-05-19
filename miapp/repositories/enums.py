from enum import Enum
from django.db import models

class Estado(models.TextChoices):
        NUEVA      = 'nueva',      'Nueva'
        EN_PROCESO = 'en_proceso', 'En proceso'
        RESUELTA   = 'resuelta',   'Resuelta'
        CANCELADA  = 'cancelada',  'Cancelada'

class Prioridad(models.TextChoices):
        BAJA    = 'baja',    'Baja'
        MEDIA   = 'media',   'Media'
        ALTA    = 'alta',    'Alta'
        URGENTE = 'urgente', 'Urgente'

class Categoria(models.TextChoices):
        EQUIPOS       = 'equipos',       'Equipos'
        RED           = 'red',           'Red'
        HVAC          = 'hvac',          'HVAC'
        ILUMINACION   = 'iluminacion',   'Iluminación'
        SEGURIDAD     = 'seguridad',     'Seguridad'
        MANTENIMIENTO = 'mantenimiento', 'Mantenimiento'
        OTRA          = 'otra',          'Otra'
    