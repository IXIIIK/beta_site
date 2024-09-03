from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def image_upload(request):
    return render(request, "index.html")


def about_views(request):
    return render(request, "about.html")


def contact_views(request):
    return render(request, "contact.html")
