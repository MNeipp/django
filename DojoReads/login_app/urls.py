from django.urls import path
from reads_app import views as ra_views
from . import views as login_views

urlpatterns =[
    path('',login_views.index),
    path('process/', login_views.process, name="process"),
    path('login/',login_views.login, name="login"),
    path('logout/',login_views.logout, name="logout"),
    path("users/<int:user_id>", ra_views.user_info),
]