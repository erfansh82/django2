from atexit import register
from django.contrib import admin
from .models import document


admin.site.register(document)