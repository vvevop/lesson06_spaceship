from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils import timezone

def index_page(request: HttpRequest) -> HttpResponse:
    context: dict[str, str | datetime] = {
        "time" : timezone.now(),
        "fuel" : request.GET.get("fuel", "100")
    }

    return render(request, 'spaceship/index.html', context)

def fuel_page(request: HttpRequest) -> HttpResponse:
    distance = int(request.GET.get("distance", 0))
    consumption = int(request.GET.get("consumption", 0))

    context: dict[str, int] = {
        "distance" : distance,
        "consumption" : consumption,
        "needed_fuel" : distance * consumption  
    }

    return render(request, 'spaceship/fuel.html', context)