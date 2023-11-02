import os

from django import get_version
from django.conf import settings
from django.shortcuts import render
from pages.kayak import *

def home(request):
    ockayak = Kayak()
    ockayak.brand = "Ocean Kayak"
    ockayak.material = "Single Layer Polyethylene"
    ockayak.length = "12 ft."

    malibu = PaddleKayak()
    malibu.model = "Malibu"
    malibu.capacity = 1
    malibu.style = "Sit-on-Top"
    malibu.activity = "Recreation"

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"] + " | Paddle Kayak Model and Style: " + malibu.model + " " + malibu.style,
    }

    return render(request, "pages/home.html", context)
