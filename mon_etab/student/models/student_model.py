from django.db import models

from base.models.person_model import Person


class Student(Person):
    matricule = models.CharField(max_length=255)
    phone_number_father = models.CharField(max_length=255)

    def __str__(self): 
        return f"{ self.matricule} : {self.phone_number_father}"