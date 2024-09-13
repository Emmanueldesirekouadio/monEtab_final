from django.db import models

choices_sexe = [
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Other', 'OTHER')
]

class Gender(models.Model):
    sexe = models.CharField(max_length=30, choices=choices_sexe)

    class Meta :
        abstract = True

    def __str__(self):
        return self.sexe


    