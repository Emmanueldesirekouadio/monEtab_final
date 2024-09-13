from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from ..models.student_model import Student
from ..forms.student_form import StudentForms
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting
# Create your views here.


@login_required()
def list_student(request):
    search_area = request.GET.get('name')
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()


    if search_area:
        search_student = Student.objects.filter(user__pseudo__icontains = search_area )
        count_student = search_student.count()
        context = {
            'students':search_student,
            'count_student': count_student,
            'school_total': school_total,
        }

    else:
        students = Student.objects.all()
        count_student = students.count()
        context = {
            'students': students,
            'count_student': count_student,
            'app_setting_total': app_setting_total,
            'school_total' : school_total,
        }
    return render(request, 'student/list_student.html', context)


@login_required()
def add_student(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    student = StudentForms()

    if request.method == 'POST':
        student = StudentForms(request.POST)
        if student.is_valid():
            student.save()
            return redirect('student:list_student')

    context = {
        'title': 'Ajouter un Eleve',
        'student': student,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'student/add_student.html',context)


@login_required()
def update_student(request, id):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()
    context = {
        "title": 'Modifier Professeur',
        "app_setting_total": app_setting_total,
        "school_total": school_total,
    }
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Student does not exist !!")
        return redirect('teacher:list_teacher')

    if request.method == 'POST':
        student_form = StudentForms(data=request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student:list_student')
    student_form = StudentForms(instance=student)
    context["student"] = student_form

    return render(request, 'student/add_student.html', context)


@login_required()
def delete_student(request,id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Student does not exist !!")
        return redirect('teacher:list_teacher')

    student.delete()
    return redirect('student:list_student')
