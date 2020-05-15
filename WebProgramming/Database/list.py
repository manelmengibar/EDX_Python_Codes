
#Con este programa podremos leer los valores de una tabla (Que se encuentra en una base de datos)
#Esta base de datos es creada y modificada mediante comandos sql (ejemplo fichero: create.sql) cuyos
#comandos se copian en el terminal una vez ejecutado el comando psql


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#aquí creamos el motor encargado de interactuar con la base de datos
#donde pone DATABAS_URL deberiamos poner la url en la que se encuentra nuestra base de datos.
engine = create_engine("postgresql://localhost/python")
#esto permite acceder con diferentes sesiones/usuarios a la base de datos
db = scoped_session(sessionmaker(bind=engine))

#función que nos devolverá todos los valores de la tabla
def main():
    #Indicamos la base de datos de la cual cogemos la tabla de valores mediante la instrucción sql
    #Fetchall() sirve para indicar que queremos que nos devuelva todos los valores.
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    #hacemos un loop para imprimir todos los valores tomados de la tabla
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
