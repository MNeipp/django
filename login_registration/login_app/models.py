from __future__ import unicode_literals
from django.db import models
import bcrypt, re, datetime

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def basic_validator(self, postData):
        today = datetime.date.today()
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be at least 2 characters long"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be at least 2 characters long"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email__exact=(postData['email'])).exists():
            errors['email'] = "That e-mail address is already registered"
        if len(postData['DOB']) > 0 :
            dob = datetime.datetime.strptime(postData['DOB'], "%Y-%m-%d").date()
            if today.year - dob.year < 13:
                errors['DOB'] = "You must be at least 13-years-old to register an account"
        if len(postData['DOB']) < 1:
            errors['DOB'] = "Please enter a valid date"
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long"
        if postData['password'] != postData['confirm_password']:
            errors['passwords'] = "Passwords don't match."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=59)
    DOB = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    objects = userManager()

