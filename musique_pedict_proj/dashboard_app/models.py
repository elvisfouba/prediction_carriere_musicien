# Create your models here.
from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER = (
			(0, 'Femelle'),
			(1, 'Male'),
		)

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    sexe = models.PositiveBigIntegerField(choices=GENDER, null=True)
    taille_doigts = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    frappe = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    vocal = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    mouvement_jambes= models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    clavier = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_musique_model.joblib')
        self.predictions = ml_model.predict([[self.sexe ,self.taille_doigts, self.frappe, self.vocal, self.mouvement_jambes, self.clavier]])
        return super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return self.name
				
