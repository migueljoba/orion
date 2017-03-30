from django.contrib import admin

# Register your models here.
from .models import Contribuyente, ContribuyenteTipo

admin.site.register(Contribuyente)
admin.site.register(ContribuyenteTipo)