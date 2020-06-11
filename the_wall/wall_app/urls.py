from django.urls import path
from login_app import views as login_views
from . import views as wall_views

urlpatterns=[
    path('', login_views.success, name="wall"),
    path("message/", wall_views.message),
    path("comment/", wall_views.comment),
    path("delete/", wall_views.delete_message, name="delete"),

]