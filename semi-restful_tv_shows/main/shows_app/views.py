from django.shortcuts import render, redirect, HttpResponse
from . models import Show, Network
from django.contrib import messages

# Create your views here.

def index(request):
    context={
    "shows":Show.objects.all()
    }
    return render(request, "index.html", context)

def new_show(request):
    context={
        "header": "Add a New Show",
        "button": "Create",
        "form_url": "/new/process/",
    }
    return render(request, "new_show.html", context)

def create_show(request):
    #validate for errors
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else: 
        if Network.objects.filter(name__iexact=request.POST['network']).exists():
            network = Network.objects.get(name__iexact=request.POST['network'])
        else:
            network = Network.objects.create(name=request.POST['network'])
        title = request.POST['title']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        new_show = Show.objects.create(title=title, network=network ,release_date=release_date, desc=desc) 
    return redirect(f"/shows/{new_show.id}")

def show_info(request, show_id):
    context={
        "show" : Show.objects.get(id=show_id)
    }
    return render(request, "show_info.html",context)

def edit_show(request, show_id):
    context={
    "show" : Show.objects.get(id=show_id),
    "header": f"Edit Show {show_id}",
    "button": "Update",
    "show_link": "Go to Show",
    "form_url": f"/shows/{show_id}/edit/process/",
}
    return render(request, "new_show.html", context)

def edit_show_process(request, show_id):
        #validate for errors
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit/")
    else: 
        if request.method=="POST":
            edited_show = Show.objects.get(id=show_id)
            edited_show.title = request.POST['title']
            edited_show.network.name = request.POST['network']
            edited_show.release_date = request.POST['release_date']
            edited_show.desc = request.POST['desc']
            edited_show.save()
    return redirect(f"/shows/{show_id}")

def delete_show(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect("/shows/")