import os

from django import get_version
from django.conf import settings
from django.shortcuts import render
from pages.kayak import *

def home(request):
    ockayak = Kayak("Ocean Kayak", "Single Layer Polyethylene", "12 ft.")
    malibu = PaddleKayak("Malibu", 1, "Sit-on-Top", "Recreation")

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"] + " | Paddle Kayak Model and Style: " + malibu.model + " " + malibu.style,
    }

    return render(request, "pages/home.html", context)
