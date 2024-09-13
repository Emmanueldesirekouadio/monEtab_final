from django.db import models

from base.models.helpers.date_time_model import DateTimeModel
from school.models.school_model import School
from .roleUser_model import RoleUser
from django.contrib.auth.models import AbstractUser

class UserApps(AbstractUser):
    role = models.ManyToManyField(RoleUser)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)


    # relation One to One with Person Class

    # person_id = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='user_person_ids')

    def __str__(self) -> str:
        return f"{self.username} : {self.date_joined}"


 