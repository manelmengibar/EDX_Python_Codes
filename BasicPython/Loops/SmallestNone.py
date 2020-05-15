
#inicialitzem la variable smallest amb cap valor "None"
smallest = None

print("Before")

for value in [9, 41, 12, 3, 74, 15]:

    # Amb aquest if passem a donar-li el primer número de la iteració for
    #a la variable small que fins ara tenia com a valor "None"
    #Aquesta línea només s'executarà un cop, al principi.
    if smallest is None:

        smallest = value

    elif value < smallest:

        smallest = value

    print (smallest, value)

print ("After", smallest)
