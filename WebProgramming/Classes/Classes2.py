#En este caso la classe flight también incluye el mostrar en pantalla sus subcategorias

class Flight:

    #self corresponde a la entidad misma de flight y los otros tres parametros
    #serán las subcategorias de flight.
    def __init__(self, origin, destination, duration):

        #Con esto indicamos las tres categorias = a los inputs del user.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

def main():

    #De este modo es más rapido si tenemos que introducir varios vuelos.

    f1 = Flight(origin="New York", destination="Paris", duration=540)
    #con el .print_info llamamos a la función de imprimir creada dentro de la classe
    #igual que hacemos con las subcategorias.
    f1.print_info()

    f2 = Flight(origin="Tokyo", destination="Shanghai", duration=185)
    f2.print_info()



#Esto sirve para indicar que una vez el programa ha sido importado lo unico que queremos ejecutar
#es la funcion main()
if __name__ == "__main__":
    main()
