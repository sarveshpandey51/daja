from django.db import models

# Basically models are instentizors in Django , you can call them in the method defined in the views.py 

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100) 
    details = models.CharField(max_length=500) 
    
