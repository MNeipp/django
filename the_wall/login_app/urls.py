from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('process/', views.process, name="process"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
]