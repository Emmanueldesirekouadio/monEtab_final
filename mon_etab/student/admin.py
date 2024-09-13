from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(absence_model.Absence)
admin.site.register(student_model.Student)
admin.site.register(studentCards_model.StudentCards)



