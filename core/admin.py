from django.contrib import admin

from django.db import models
from django.forms import URLField

from core.models import Categoria, Editora

admin.site.register(Categoria)
admin.site.register(Editora)
