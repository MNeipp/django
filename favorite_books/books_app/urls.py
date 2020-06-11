from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name="dashboard"),
    path('add_book/', views.add_book, name="add_book"),
    path('<int:book_id>/', views.book_info),
    path('<int:book_id>/update/', views.book_update),
    path('<int:book_id>/delete/',views.delete_book),
    path('<int:book_id>/like/', views.like_book),
    path('<int:book_id>/unlike/', views.unlike_book),
    path('user_info', views.user_info),


]