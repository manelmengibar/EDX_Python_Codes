import math

def is_prime(n):

    if n < 2:
        return False
    #Tenemos que añadir 1 a la raiz dado que el loop for excluye el último número del listado
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
