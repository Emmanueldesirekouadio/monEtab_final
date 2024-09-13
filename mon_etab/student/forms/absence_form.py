from django import forms 
from ..models.absence_model import Absence

class AbsenceForms(forms.ModelForm):
    class Meta:
        model = Absence
        fields = "__all__"  