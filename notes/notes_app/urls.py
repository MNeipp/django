from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='dashboard'),
    path('<int:note_id>/update/',views.update_content, name='update_content'),
    path('<int:note_id>/delete/',views.delete_note, name='delete_note'),
]