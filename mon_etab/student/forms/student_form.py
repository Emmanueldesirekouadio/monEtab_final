from django import forms 
from ..models.student_model import Student

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" 