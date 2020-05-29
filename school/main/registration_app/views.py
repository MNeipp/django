from django.shortcuts import render, HttpResponse, redirect
from registration_app.models import Subject, Student, Teacher

# Create your views here.
def index(request):
    return render(request, "index.html")

def subject_catalog(request):
    context={
        "subjects": Subject.objects.all()
    }
    return render(request, "subject_catalog.html")

def subjects(request, subject_id):
    current_subject = Subject.objects.get(id=subject_id)
    context={
        "subject": current_subject
    }
    return render(request, "subjects.html", context)

def create_subject(request):
    if request.method=="POST":
        name = request.POST['name']
        desc = request.POST['desc']
        new_subject = Subject.objects.create(name=name, desc=desc)
    return HttpResponseRedirect("/")

def teacher_directory(request):
    context={
        "teachers": Teacher.objects.all()
    }
    return render(request, "teacher_directory.html", context)

def teachers(request, teacher_id):
    current_teacher = Teacher.objects.get(id=teacher_id)
    context={
        "teacher": current_teacher
    }
    return render(request, "teachers.html",context)

def hire_teacher(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_teacher = Teacher.objects.create(first_name=first_name, last_name=last_name)
    return HttpResponseRedirect("/")

def student_directory(request):
    context={
        "students":Student.objects.all()
    }
    return render(request, "student_directory.html", context)

def students(request, student_id):
    current_student = Student.objects.get(id=student_id)
    context={
        "student": current_student
    }
    return render(request, "students.html", context)

def register_student(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        grade = request.POST['grade']
        new_student = Student.objects.create(first_name=first_name, last_name=last_name, grade=grade)
    return redirect("/students")