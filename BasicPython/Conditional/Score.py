score = input("Introdueix una puntuació\n")

#comprobació del format de les dades introduïdes
try:

    tscore = float(score)

except:

    tscore = -1


#En cas de format correcte
if tscore >= 0:

    #En cas de valor fora del rang demanat
    if float(score) > 1 or float(score) < 0:

        print ("Valor fora de rang!")

    #En cas de que el valor estigui dins del rang demanat
    else :

        if float(score) < 0.6:

            print (" Score grade :  F")

            print ("Cal que t'esforcis més")

        elif float(score) >= 0.6 and float(score) < 0.7:

            print (" Score grade :  D")

            print ("Segueix estudiant")

        elif float(score) >= 0.7 and float(score) < 0.8:

            print (" Score grade :  C")

            print ("Bé!""")

        elif float(score) >= 0.8 and float(score) < 0.9:

            print (" Score grade :  B")

            print ("Bona feina!")

        elif float(score) >= 0.9:

            print (" Score grade :  A")

            print ("Enhorabona!")




#En cas de format incorrecte

else:

    print ("Les dades introduïdes tenen un format incorrecte.")
