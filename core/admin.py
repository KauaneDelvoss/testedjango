from django.contrib import admin

from django.db import models
from django.forms import URLField

from core.models import Categoria, Editora, Autor, Livros

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livros)
