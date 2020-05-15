
class Flight:

    #self corresponde a la entidad misma de flight y los otros tres parametros
    #serán las subcategorias de flight.
    def __init__(self, origin, destination, duration):

        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():

    #creamos una variable  del tipo flight.
    f = Flight(origin="New York", destination="Paris", duration=540)

    f.duration += 10

    print(f.origin)
    print(f.destination)
    print(f.duration)

#Esto sirve para indicar que una vez el programa ha sido importado lo unico que queremos ejecutar
#es la funcion main()
if __name__ == "__main__":
    main()
