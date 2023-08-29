from django.shortcuts import render
from .models import Image


def index(request):
    return render(request, "main_page.html")


def gallery(request):
    photos = Image.objects.all()
    context = {
        'data': photos
    }
    print(context)
    return render(request, 'gallery_page.html', context)

