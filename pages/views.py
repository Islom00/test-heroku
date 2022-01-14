from django.shortcuts import render

from pages.models import Pictures


def home(request):
    pictures = Pictures.objects.all()
    context = {
        "pictures": pictures,
    }
    return render(request, "home.html", context)

