from dataclasses import fields
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
			class Meta:
				model = Data
				fields = ['name', 'sexe', 'taille_doigts', 'frappe', 'vocal', 'mouvement_jambes', 'clavier']