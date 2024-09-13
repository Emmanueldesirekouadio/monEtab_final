from django.db import models
from .student_model import Student
from base.models.helpers.date_time_model import DateTimeModel



class StudentCards(DateTimeModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    reference = models.CharField(max_length=255)
    issue_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.reference} : {self.student}"
