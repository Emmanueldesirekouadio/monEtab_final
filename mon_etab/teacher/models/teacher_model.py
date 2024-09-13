from django.db import models

from base.models.person_model import Person

class Teacher(Person):
    available = models.BooleanField(default=False)
    speciality = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.available} : {self.speciality}"
    