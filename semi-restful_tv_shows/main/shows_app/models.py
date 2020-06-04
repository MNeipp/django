from __future__ import unicode_literals
from django.db import models
import datetime
from datetime import date


# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}
        today = datetime.date.today()
        today = today.strftime("%Y-%m-%d")
        if postData['id']:
            current_show = Show.objects.get(id=postData['id'])
        else:
            current_show = None
        if len(postData['title']) < 2:
            errors['title'] = "Title of show must be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network name must be at least 3 characters"
        if len(postData['desc']) < 10 and postData['desc'].strip() != "":
            print(postData['desc'])
            errors['desc'] = "Description optional but must be at least 10 characters."
        if postData['release_date'] >= today:
            errors ['release_date'] = "Release Date must be prior than today"
        if Show.objects.filter(title__iexact=postData['title']).exists():
            if current_show != None:
                if Show.objects.filter(title__iexact=postData['title']).exists() and postData['title'] != current_show.title:
                    errors['title'] = "That show already exists."
            else:
                errors['title'] = "That show already exists."
        return errors

class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(null=True)
    network = models.ForeignKey(Network, related_name="has_shows",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()