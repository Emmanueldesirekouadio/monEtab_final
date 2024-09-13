from django import forms 

from ..models.appSetting_model import AppSetting

class AppSettingForm(forms.ModelForm):
    class Meta:
        model = AppSetting
        fields = "__all__"