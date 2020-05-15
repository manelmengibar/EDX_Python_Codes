
#le pedimos al usuario que introduzca un número
m = input("write a number\n")

#convertimos el valor introducido a integer
n = int(m)

#hacemos una cuenta atrás desde el valor introducido hasta llegar  a 0
while n > 0:

    print (n)

    n = n - 1

#Una vez el valor es igual a 0 se muesra en terminal lo siguiente:
print ("Blastoff!")

exit()
