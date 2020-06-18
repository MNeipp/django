from django.urls import path
from . import views as db_views

urlpatterns =[
    path('',db_views.home,name="home"),
    path('dashboard/',db_views.dashboard, name="dashboard"),
]