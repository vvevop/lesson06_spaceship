from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('fuel/', views.fuel_page, name='fuel')
]