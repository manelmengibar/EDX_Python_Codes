from django.urls import path

from . import views

urlpatterns = [

    #amb aquestes URL indiquem quina funció volem xecutar del codi de python (views.py)
    #entre cometes trobem el que haurem d'escriure a la URL per accedir a cada informació
    #ejemple: http://127.0.0.1:8000/2  --> amb això accediriem a la info del vol amb id 2.
    #name indica el nom que li volem dinar a aquesta URL per identificarla a la resta del codi.
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]
