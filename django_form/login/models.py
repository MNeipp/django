from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def name_validator(name):
    if len(name) < 3:
        raise ValidationError(
        'Must be longer than 3 characters'
    )

def password_validator(password):
    if len(password) < 8:
        raise ValidationError(
        'Password must be at least 8 characters'
    )


class User(models.Model):
    first_name = models.CharField(max_length=255, validators=[name_validator])
    last_name = models.CharField(max_length=255, validators=[name_validator])
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length=255, validators = [password_validator])
