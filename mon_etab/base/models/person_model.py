from django.db import models

from base.models.helpers.adresse_model import Adresse
from user.models.user_model import UserApps
from .helpers.gender_model import Gender
from .helpers.date_time_model import DateTimeModel


class Person(Gender,DateTimeModel):
    # Relation one to one with Adresse class


    adresse = models.OneToOneField(Adresse,on_delete=models.CASCADE,related_name="%(class)s_person_adress_ids")
    user = models.OneToOneField(UserApps,on_delete=models.CASCADE,related_name="%(class)s_person_user_ids")


    birthday = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    url_picture = models.CharField(max_length=255) 



    


    class Meta :  
        abstract = True

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

