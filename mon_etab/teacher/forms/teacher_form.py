from django import forms

from ..models.teacher_model import Teacher

class TeacherForms(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"