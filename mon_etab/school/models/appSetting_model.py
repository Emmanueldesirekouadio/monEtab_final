from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

# from .school import School

class AppSetting(DateTimeModel):
    smtp_server = models.CharField(max_length=255)
    smtp_port = models.IntegerField()
    smtp_username = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.smtp_server} : {self.smtp_username}"
    



  
