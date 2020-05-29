from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('students/', views.student_directory),
    path('subjects/', views.subject_catalog),
    path('teachers/', views.teacher_directory),
    path('students/<int:student_id>', views.students),
    path('subjects/<int:subject_id>', views.subjects),
    path('teachers/<int:teacher_id>', views.teachers),
    path('register_student/', views.register_student),
    path('hire_teacher/', views.hire_teacher),
    path('create_subject/', views.create_subject),

]