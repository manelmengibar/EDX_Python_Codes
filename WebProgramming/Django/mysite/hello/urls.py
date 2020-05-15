from django.urls import path

from . import views

urlpatterns = [
    #indicamos que cuando el usuario vaya a una URL vacía (/) se muestre la info
    #que hay en el fichero views.py en la función index
    path("", views.index)
]
