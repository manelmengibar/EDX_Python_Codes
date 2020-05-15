astr = "Hello Bob"

# Hacemos que pruebe esta linea de código
try:

    istr = int(astr)

#En caso dado que "Hello bob" es una variable de tipo str y no int, no funcionará, motivo por el cual
#ejecutara la siguiente instrucción y nos devolverá un -1 en vez de Hello Bob
except:

    istr = -1


print ("First", istr)
