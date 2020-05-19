
#Comandos para interactuar con las bases de datos:
#Estos comandos se tienen que copiar directamente en el terminal una vez activada la base de datos
#o se puede crear un programa python que introduzca los comandos automaticamente.

#---------------------------------------------------------------------------------------------------

#Creacion de una tabla llamada flights

CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  origin VARCHAR NOT NULL,
  destination VARCHAR NOT NULL,
  duration INTEGER NOT NULL
);

#---------------------------------------------------------------------------------------------------

#Insertar valores a la tabla llamada flights

INSERT INTO flights (origin, destination, duration) VALUES ('Barcelona','Seoul','780');

#---------------------------------------------------------------------------------------------------

#Mostrar todos los valores de la tabla flight (* nos indica que queremos visualizar todos los valores)

SELECT * FROM flights;

#---------------------------------------------------------------------------------------------------

#Actualizar valores de la tabla flights

UPDATE flights
  SET duration = 430
  WHERE origin = 'New York'
  AND destination = 'London';

#---------------------------------------------------------------------------------------------------

#Creamos una tabla para los pasajeros

CREATE TABLE passengers (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flight_id INTEGER REFERENCES flights
);
