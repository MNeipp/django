from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:page_number>', views.ajax_paginator, name="page")
]