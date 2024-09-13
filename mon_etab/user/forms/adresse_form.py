from django import forms 

from base.models.helpers.adresse_model import Adresse

class AdresseForms(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = "__all__"