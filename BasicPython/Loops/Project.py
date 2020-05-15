

#inicialitzem les variables sense cap valor
valor = None
minimo = None
maximo = None

#Comencem un loop que s'executarà mentre l'usuari no introdueixi la paraula "hecho"
while valor != "hecho":


    #aquí demanem que l'usuari insereixi un valor o "hecho"
    svalor = input ("Introduzca un número o bien - hecho-  para terminar:  ")

    # El primer pas comprova que l'usuari no hagi escollit acabar.
    if svalor == "hecho":

        break #amb aquest break sortiriem del loop






    #Un cop l'usuari ha decidit no acabar amb el programa comprovem quin tipus de dades
    #ha inserit
    try:

        #mirem si les dades inserides son del tipus integer
        test = int(svalor)

    except:

        #de no ser així aquest mòdul assignarà valor -1 a la variable test
        test = -1





    #si test és igual a -1 vol dir que el tipus de dada inserida no és del tipus int i per tant
    #salta un missatge d'avis i no s'executarà la resta del codi. Sortim del loop.
    if test == -1:

        print ("Invalid input")

    #Si el valor inserit és de tipus int s'executa la resta del codi
    else:

        #IMPORTANT creem una variable per determinar que l'input de l'usuari és de tipus int.
        #De no fer aquest pas ho tractaria com a strings i les comparacions no serien correctes
        nvalor = int(svalor)

        #Aquí inicialitzem les variables minimo y maximo amb el primer input de l'usuari.
        #Aquesta línia només s'executa una vegada, al principi de tot.
        if minimo == None and maximo == None:

            minimo = nvalor
            maximo = nvalor

        #Si el valor afegit es més gran que l'enregistrat a la variable maximo es substitueix
        #per l'actual valor.
        elif nvalor > maximo:

            maximo = nvalor
        #Si el valor afegit es més petit que l'enregistrat a la variable maximo es substitueix
        #per l'actual valor.
        elif nvalor < minimo:

            minimo = nvalor


#Un cop acabat el codi imprimeix el valor més gran i el més petit de tots els inserits.
print ( "Maximum is:", maximo)
print ( "Minimum is:", minimo)
