from django import forms 

from ..models.user_model import UserApps

class UserAppForms(forms.ModelForm):
    class Meta:
        model = UserApps
        fields = ("username","password","is_active")