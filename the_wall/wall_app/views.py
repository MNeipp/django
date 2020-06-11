from django.shortcuts import render, redirect
from .models import Comment, Message
from login_app.models import User

# Create your views here.
def message(request):
    logged_user = User.objects.get(id = request.session["user_id"])
    new_message = Message.objects.create(user = logged_user, content = request.POST["message_content"])
    
    return redirect("/wall/")

def comment(request):
    logged_user = User.objects.get(id = request.session["user_id"])
    current_message = Message.objects.get(id=request.POST["message_id"])
    new_comment = Comment.objects.create(message = current_message, user = logged_user, content = request.POST["comment_content"])
    return redirect("/wall/")

def delete_message(request):
    Message.objects.get(id = request.POST['message_id']).delete()
    return redirect("/wall/")
