from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index),
    path('authors/', views.authors),
    path('authors/<int:author_ID>', views.author_info),
    path('books/<int:book_ID>', views.book_info),
    path('add_book/', views.add_book),
    path('add_author/', views.add_author),
    path('authors/<int:author_ID>/add_work/', views.add_work),
    path('books/<int:book_ID>/add_const_author/', views.add_contributing_author),
]