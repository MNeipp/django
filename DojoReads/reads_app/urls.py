from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('add/',views.add_book,name="add_book"),
    path('add/process/', views.add_book_process),
    path('<int:book_id>', views.book_reviews),
    path('<int:book_id>/add_review/', views.add_review),
    path('<int:current_book_id>/<int:review_id>/delete_review/',views.delete_review),
]
