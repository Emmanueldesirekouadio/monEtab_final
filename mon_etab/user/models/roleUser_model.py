from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

class RoleUser(DateTimeModel):
    role = models.CharField(max_length=255) 

    def __str__(self) -> str:
        return self.role

    
