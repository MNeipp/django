from __future__ import unicode_literals
from django.db import models
import bcrypt, re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name needs to be at least 2 characters long"
        result_alias = User.objects.filter(alias__iexact=(postData['alias']))
        if len(result_alias) > 0:
            errors['alias'] = "That alias is already in use"
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias needs to be at least 2 characters long"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        result_email = User.objects.filter(email__iexact=(postData['email']))
        if len(result_email) > 0:
            errors['email'] = "That e-mail address is already registered"
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long"
        elif postData['password'] != postData['confirm_password']:
            errors['passwords'] = "Passwords don't match."
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    objects = userManager()

