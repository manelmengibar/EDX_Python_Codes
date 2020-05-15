
largest = 0

print ("The largest number before running code is:", largest)

# Afegim la variable the_num i li donem tots els valors que apareien entre []
#El codi farà un loop amb tots aquests valors.
for the_num in [9, 41, 12, 3, 74, 15]:
    #Analitzem si el valor analitzat es més gran que el més gran fins el moment
    if the_num > largest:
        #Cada cop que un sigui més gran l'associem a la variable "largest"
        largest = the_num
    #Afegim el valor més gran fins el moment i el que estem analitzant.
    print (largest, the_num)
#finalment mostrem el número més gran de tots els analitzats.
print ("Afther running code the largest number is:", largest)
