from django.db import models
from login_app.models import User

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    board = models.ForeignKey(User, related_name="board_posts", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name="has_posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name="has_comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="has_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

