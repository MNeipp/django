from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('new/', views.new_show),
    path('<int:show_id>/',views.show_info),
    path('<int:show_id>/edit/', views.edit_show),
    path('<int:show_id>/destroy/', views.delete_show),
    path('new/process/', views.create_show),
    path('<int:show_id>/edit/process/', views.edit_show_process),
    path('<int:show_id>/destroy/', views.delete_show)
]