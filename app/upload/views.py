from django.shortcuts import render
from .models import PostModel, Category


def image_upload(request):
    post_content = PostModel.objects.all()

    context = {
        'products': post_content,
    }

    return render(request, "index.html", context)


def about_views(request):
    return render(request, "about.html")


def contact_views(request):
    return render(request, "contact.html")
