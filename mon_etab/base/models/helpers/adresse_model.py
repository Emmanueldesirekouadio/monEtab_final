from django.db import models

class Adresse(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    
