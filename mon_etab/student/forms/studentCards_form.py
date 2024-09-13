from django import forms 
from ..models.studentCards_model import StudentCards

class StudentCardsForms(forms.ModelForm):
    class Meta:
        model = StudentCards
        fields = "__all__" 