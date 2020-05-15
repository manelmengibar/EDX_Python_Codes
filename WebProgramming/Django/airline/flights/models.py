from django.db import models

# Create your models here.


#Creamos una clase para aeropuertos
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    #Como se va a mostrar la info sobre el aeropuerto.
    def __str__(self):
        return f"{self.city} ({self.code})"



#Creamous una clase para vuelos
class Flight(models.Model):
    #Tanto origen como destino dependeran ahora de la clase airport
    #On_delete permite controla que sucede si elimino un aeropuerto y sigue habiendo vuelos
    #con este.
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    #esto definirá como se ve la info de esta clase en pantalla
    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination} : {self.duration}"


#Creamos una clase para pasajeros.
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    #ManyToManyField permite que la info se guarde tanto en la tabla de Passenger como en la de Flight
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
         return f"{self.first} {self.last}"
