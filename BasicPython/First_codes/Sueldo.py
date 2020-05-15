
#Pedimos al usuario que introduzca las horas trabajadas
hrs = input("Cuantas horas ha trabajado?\n")

#Pedimos al usuario el precio por hora trabajada
tasa = input ("Cual es el salario por hora trabajada?\n")

#Hacemos un calculo de hora por precio/hora para saber el salario.
#Convertimos las variables de hrs y tasa a float.
Salario = float(hrs) * float(tasa)

#Mostramos al usuario el sueldo.
print ("Su salario esta semana va a ser: ", Salario, "€\n", "Hasta la próxima!")
