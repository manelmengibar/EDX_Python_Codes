
#Pedimos al usuario que introduzca un número
rawstr = input ("Enter a number")

#En esta parte del códio comprobamos si el valor introducido es de tipo introduzca
#de no ser así nos devuelve un -1
try:
    ival = int (rawstr)
except:
    ival = -1

# Aquí comprobamos si el usuario ha introducido un número o una variable de otro tipo (-1)
if ival > 0:
    print ("Nice work")
else:
    print ("Not a number")
