from __future__ import unicode_literals
from django.db import models
import bcrypt, re, datetime

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def basic_validator(self, postData):
        today = datetime.datetime.today().date()
        min_dob = datetime.datetime(today.year-13, today.month, today.day).date()
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be at least 2 characters long"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be at least 2 characters long"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        result = User.objects.filter(email__iexact=(postData['email']))
        if len(result) > 0:
            errors['email'] = "That e-mail address is already registered"
        if len(postData['DOB']) > 0 :
            dob = datetime.datetime.strptime(postData['DOB'], "%Y-%m-%d").date()
            if min_dob < dob:
                errors['DOB'] = "You must be at least 13-years-old to register an account"
        if postData['DOB'] == "":
            errors['DOB'] = "Please enter a valid date"
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long"
        elif postData['password'] != postData['confirm_password']:
            errors['passwords'] = "Passwords don't match."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    DOB = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    objects = userManager()

