from django.shortcuts import render, redirect, HttpResponse
from courses_app.models import Course, Description, Comment
from django.contrib import messages

# Create your views here.
def index(request):
        context ={
            "courses": Course.objects.all()
        }
        return render (request, "index.html",context)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect("/")
        
    name = request.POST['name']
    desc = request.POST['desc']
    new_course = Course.objects.create(name=name)
    Description.objects.create(course=new_course, desc=desc)
    return redirect("/")

def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    context={
        "course": course
    }
    return render(request, "destroy.html", context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect("/")

def comments(request, course_id):
    course = Course.objects.get(id=course_id)
    context ={
        "course": course
    }
    return render(request, "comments.html",context)

def add_comment(request, course_id):
    course = Course.objects.get(id=course_id)
    comment = request.POST['comment']
    Comment.objects.create(course = course, text=comment)
    return redirect(f'/course/comments/{course_id}/')
