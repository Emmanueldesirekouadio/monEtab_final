from django import forms 

from ..models.school_model import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"