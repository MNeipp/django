from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Lead


def index(request):
    leads = Lead.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(leads,5)
    try:
        leads = paginator.page(page)
    except PageNotAnInteger:
        leads = paginator.page(1)
    except EmptyPage:
        leads = paginator.page(paginator.num_pages)
    context = {
        "leads": leads,
    }
    return render(request, "index.html", context)

def ajax_paginator(request,page_number):
    leads = Lead.objects.all()
    page = request.GET.get('page',page_number)
    paginator = Paginator(leads,5)
    try:
        leads = paginator.page(page)
    except PageNotAnInteger:
        leads = paginator.page(1)
    except EmptyPage:
        leads = paginator.page(paginator.num_pages)
    context = {
        "leads": leads,
    }
    return render(request, "table_snippet.html", context)