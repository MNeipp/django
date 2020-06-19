from django.urls import path
from . import views as db_views

urlpatterns =[
    path('',db_views.home,name="home"),
    path('dashboard/',db_views.dashboard, name="dashboard"),
    path('users/edit/', db_views.profile, name="profile"),
    path('users/edit/update_info/', db_views.update_info, name="update_info"),
    path('users/edit/update_description/', db_views.update_description, name="update_description"),
    path('users/edit/update_password/', db_views.update_password, name="update_password"),
    
]