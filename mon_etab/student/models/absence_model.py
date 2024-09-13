from django.db import models
from .student_model import Student
from base.models.helpers.date_time_model import DateTimeModel


class Absence(DateTimeModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='absence_student_ids') 
    
    absence_date = models.DateTimeField(auto_now_add=True)
    absence_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{ self.absence_number} : {self.absence_date}"
    