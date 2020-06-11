from __future__ import unicode_literals
from django.db import models
from login_app.models import User

# Create your models here.
class bookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if postData['book_title'] == "":
            errors['book_title'] = "Please enter the title of the book"
        if len(postData['book_desc']) < 5:
            errors['book_desc'] = "Book description must be at least 5 characters long"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_books", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name = "liked_books")
    objects = bookManager()