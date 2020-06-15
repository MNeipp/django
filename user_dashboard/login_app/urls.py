from django.urls import path
from . import views as login_views

urlpatterns =[
    path('signin/',login_views.index),
    path('process/', login_views.process, name="process"),
    path('login/',login_views.login, name="login"),
    path('logout/',login_views.logout, name="logout"),
]