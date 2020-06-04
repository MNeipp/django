from __future__ import unicode_literals
from django.db import models

# Create your models here.
class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['name']) < 5:
            errors['name'] = "The course name must be at least 2 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "The description must be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = courseManager()

class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

