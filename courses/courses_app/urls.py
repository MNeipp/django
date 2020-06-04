from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('add_course', views.add_course, name="add_course"),
    path('course/destroy/<int:course_id>/', views.destroy, name="destroy_course" ),
    path('course/destroy/<int:course_id>/delete/', views.delete, name="delete_course" ),
    path('course/comments/<int:course_id>/', views.comments),
    path('course/comments/<int:course_id>/add/', views.add_comment),
]