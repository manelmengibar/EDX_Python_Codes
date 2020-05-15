from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

#importamos del mismo directorio y del fichero models la clase Flight
from .models import Flight, Passenger

# Create your views here.

#Función para mostrar todos los vuelos guardados.
def index(request):

    #indicamos las cosas que queremos introducir al template index.html
    context = {
        "flights": Flight.objects.all()
    }

    #utilizamos la plantilla html dentro de templates (flights>index.html)
    return render(request, "flights/index.html", context)


#Función para mostrar datos del vuelo indicado mediante (flight_id)
def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        #Esto nos va a mostrar los pasajeros que existen pero NO estan en este vuelo.
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render (request, "flights/flight.html", context)


#Función para que un usuario pueda hacer una reserva.
def book(request, flight_id):

    try:
        passenger_id = int(request.POST["passenger"])
        passengers = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)

    except KeyError:
        return render(request, "flights/error.html" , {"message": "No selection."})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html" , {"message": "No flight."})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html" , {"message": "No passenger"})

    passengers.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
