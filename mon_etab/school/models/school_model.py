from django.db import models
from .appSetting_model import AppSetting
from base.models.helpers.named_date_time import NamedDateTimeModel


class School(NamedDateTimeModel):
    app_setting = models.OneToOneField(AppSetting, on_delete=models.CASCADE, related_name="app_setting_school")

    url_logo = models.CharField(max_length=255)

    # def __str__(self) -> str:
    #     return f"{self.name}"
    
 