
#Este programa rellenará los campos de la tabla flights con los valores de un fichero
# tipo (.cvs) (file: flights.cvs).
#IMPORTANTE: lA tabla "flights" tiene que haber sido creada antes de ejecutar este código.
#En último lugar nos mostrará estos valores impresos (en el terminal)


import csv

#Modulo que nos permite interactuar con las bases de datos.
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


#aquí creamos el motor encargado de interactuar con la base de datos
#postgresql://localhost/python corresponde a la ubicación de la base de datos creada mediante
#postgresql
engine = create_engine("postgresql://localhost/python")
#esto permite acceder con diferentes sesiones/usuarios a la base de datos
db = scoped_session(sessionmaker(bind=engine))



#función que leerá los valores del csv, los insertará e la base de datos flights
#y finalmente nos lo imprimirá todo en el terminal.
def main():
    #Abre fichero con extensión .csv
    f = open("flights.csv")
    #Lee los valores que hay en flights.csv
    reader = csv.reader(f)

    #Loop para rellenar todos los campos de la tabla con los valores del csv.
    for origin, destination, duration in reader:

        #Instrucción sql para introducir valores en tabla flights
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin":origin, "destination":destination, "duration":duration})

        #imprime en pantalla los valores que habrá finalmente en la tabla.
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")

    #Amb aquesta última ordre li diem que guardi els canvis que hem fet a la base de dades
    db.commit()





if __name__ == "__main__":
    main()
