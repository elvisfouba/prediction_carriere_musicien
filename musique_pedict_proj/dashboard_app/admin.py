from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    	list_display = ('name', 'sexe', 'taille_doigts', 'frappe', 'vocal', 'mouvement_jambes','clavier','predictions')

admin.site.register(Data, DataAdmin)

# Register your models here.
