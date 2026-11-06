from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils import timezone

from .models import Ship, FuelCalculation

def index_page(request: HttpRequest) -> HttpResponse:
    context: dict[str, str | datetime] = {
        "time" : timezone.now(),
        "fuel" : request.GET.get("fuel", "100")
    }

    return render(request, 'spaceship/index.html', context)

def fuel_page(request: HttpRequest) -> HttpResponse:
    """Считает нужное топливо и сохраняет расчет в базу для корабля "Орбита-7" """
    distance = int(request.GET.get("distance", 0))
    consumption = int(request.GET.get("consumption", 0))
    needed_fuel = distance * consumption

    # Берем из базы корабль, к которому привязываем расчеты
    ship = Ship.objects.get(name="Орбита-7")

    # Создаем расчет и связываем его с кораблем
    calc = FuelCalculation(
        ship=ship,
        distance=distance,
        consumption=consumption,
        needed_fuel=needed_fuel,
        created_at=timezone.now(),
    )
    # Сохраняем расчет в базу
    calc.save()

    context: dict[str, int] = {
        "distance" : distance,
        "consumption" : consumption,
        "needed_fuel" : needed_fuel
    }

    return render(request, 'spaceship/fuel.html', context)
