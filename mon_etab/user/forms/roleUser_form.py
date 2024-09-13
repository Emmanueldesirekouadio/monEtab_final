from django import forms 

from ..models.roleUser_model import RoleUser

class RoleUserForms(forms.ModelForm):
    class Meta:
        model = RoleUser
        fields = "__all__"