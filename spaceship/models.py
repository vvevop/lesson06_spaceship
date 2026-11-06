from django.db import models


class Ship(models.Model):
    """Корабль: хранит данные о корабле"""

    # Название корабля (строка до 100 символов)
    name = models.CharField(max_length=100)


class FuelCalculation(models.Model):
    """Расчет топлива: хранит данные одного расчета"""

    # Расстояние полета (целое число, не меньше 0)
    distance = models.PositiveIntegerField()
    # Расход топлива на единицу расстояния
    consumption = models.PositiveIntegerField()
    # Сколько топлива нужно на весь полет
    needed_fuel = models.PositiveIntegerField()
    # Время создания записи (ставится автоматически при сохранении)
    created_at = models.DateTimeField(auto_now_add=True)