from django.shortcuts import render, HttpResponse, redirect
from registration_app.models import Subject, Student, Teacher, Rating

# Create your views here.
def index(request):
    context={
        "total_students":len(Student.objects.all()),
        "total_subjects":len(Subject.objects.all()),
        "total_teachers":len(Subject.objects.all()),
    }
    return render(request, "index.html", context)

def subject_catalog(request):
    context={
        "subjects": Subject.objects.all()
    }
    return render(request, "subject_catalog.html", context)

def subjects(request, subject_id):
    current_subject = Subject.objects.get(id=subject_id)
    not_teachers = Teacher.objects.exclude(subjects__id=subject_id)
    context={
        "subject": current_subject,
        "not_teachers":not_teachers,
        "all_teachers":Teacher.objects.all()
    }
    return render(request, "subjects.html", context)

def create_subject(request):
    if request.method=="POST":
        name = request.POST['name']
        desc = request.POST['desc']
        Subject.objects.create(name=name, desc=desc)
    return redirect("/subjects")

def add_subject(request, teacher_id):
    if request.method=="POST":
        current_teacher = Teacher.objects.get(id=teacher_id)
        new_subject = Subject.objects.get(id=request.POST['subject'])
        current_teacher.subjects.add(new_subject)
    return redirect(f'/teachers/{teacher_id}')

def add_teacher(request, subject_id):
    if request.method=="POST":
        current_subject = Subject.objects.get(id=subject_id)
        new_teacher = Teacher.objects.get(id=request.POST['teacher'])
        current_subject.all_teachers.add(new_teacher)
    return redirect(f"/subjects/{subject_id}")

def teacher_directory(request):
    context={
        "teachers": Teacher.objects.all()
    }
    return render(request, "teacher_directory.html", context)

def teachers(request, teacher_id):
    current_teacher = Teacher.objects.get(id=teacher_id)
    total = 0
    for ratings in current_teacher.ratings.all():
        total += ratings.rating
    if len(current_teacher.ratings.all()) == 0:
        average_rating = "Not yet rated"
    else:
        average_rating = round(total/len(current_teacher.ratings.all()),1)
    context={
        "teacher": current_teacher,
        "rating":average_rating,
        "not_subjects": Subject.objects.exclude(all_teachers__id=teacher_id)
    }
    return render(request, "teachers.html",context)

def hire_teacher(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Teacher.objects.create(first_name=first_name, last_name=last_name)
    return redirect("/teachers")

def rate_teacher(request, teacher_id):
    if request.method=="POST":
        Rating.objects.create(rating=request.POST['rating'], teacher = Teacher.objects.get(id=teacher_id))
    return redirect(f"/teachers/{teacher_id}")

def student_directory(request):
    context={
        "students":Student.objects.all()
    }
    return render(request, "student_directory.html", context)

def students(request, student_id):
    current_student = Student.objects.get(id=student_id)
    context={
        "student": current_student,
        "not_subjects": Subject.objects.exclude(all_students__id=student_id)
    }
    return render(request, "students.html", context)

def enroll_student(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        grade = request.POST['grade']
        Student.objects.create(first_name=first_name, last_name=last_name, grade=grade)
    return redirect("/students")

def register_subject(request, student_id):
    if request.method=="POST":
        current_student = Student.objects.get(id=student_id)
        new_subject = Subject.objects.get(id=request.POST['register_subject'])
        new_subject.all_students.add(current_student)
    return redirect (f"/students/{student_id}")
        