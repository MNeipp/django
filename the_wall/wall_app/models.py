from django.db import models
from login_app.models import User
from django.utils import timezone
import math

# Create your models here.

class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name="has_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    message = models.ForeignKey(Message, related_name="has_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="has_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)


