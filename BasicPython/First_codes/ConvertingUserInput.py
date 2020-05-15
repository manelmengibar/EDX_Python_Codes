#Convert elevator floors

#Le pedimos al usuario de que planta europea se trata
inp = input ("Europe floor?\n")

#A continuación el programa transforma la variable inp en integer y le añade 1
#De esta manera tenemos el piso equivalente en USA
usf = int(inp) + 1

#Finalmente mostramos el equivalente de piso en USA
print ("The equivalent US floor is", usf)
