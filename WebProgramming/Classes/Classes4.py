
#Creamos clase flight
class Flight:

    counter = 1


    def __init__(self, origin, destination, duration):

        #Definimos varias subcategorias (id, passengers, origin, etc)

        #keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1

        #Keep track of passengers.
        self.passengers = []

        #Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    #Per imprimir el vol i els passatgers associats a aquest
    def print_info(self):

        print()
        print("INFO ABOUT YOUR FLIGHT RESERVATION:")
        print()
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        print()
        print ("Passengers:")
        for Passenger in self.passengers:
            print(f"{Passenger.name}")

    #Per associar el id del vol amb el passatger
    def add_passengers(self,p):
        self.passengers.append(p)
        p.flight_id = self.id



#creamos clase passenger
class Passenger:

    def __init__(self, name):
        self.name = name

def main():

    #Create flight.
    ori=input("Set origin:")
    des=input("Set destination:")
    dur=input("Set duration:")
    f1 = Flight(origin=ori, destination=des, duration=dur)

    #Create passengers.
    Manel = Passenger(name="Manel")
    Anna = Passenger(name="Anna")

    #Add passengers to flight.
    f1.add_passengers(Manel)
    f1.add_passengers(Anna)

    #Print all the info about flight and passengers
    f1.print_info()




if __name__ == "__main__":
    main()
