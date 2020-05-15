
#definimos una nueva clase llamada flight con 3 subcategorias
class Flight:

    #self corresponde a la entidad misma de flight y los otros tres parametros
    #serán las subcategorias de flight.
    def __init__(self, origin, destination, duration):

        self.origin = origin
        self.destination = destination
        self.duration = duration
        
