from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='registration'),
    path('success', views.success, name='success')

]