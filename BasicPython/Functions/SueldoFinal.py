# Demanem a l'usuari que introdueixi hores i preu/hora
hr = input ("Hores treballades:\n")
rt = input ("Preu per hora treballada:\n")

# Amb filtre try/except comprobem si els valors introduits per l'usuari
# son númerics o no
try:

    thr = float(hr) #aquí mirem si l'hora te format float (posem una variable nova de control thr)
    trt = float(rt) #aquí mirem si el preu te format float (posem una variable nova de control trt)

# En cas de que els valors introduits no tinguin el format adient  li donarem valor -1 a les dues
# variables de control.
except:

    thr = -1
    trt = -1

#Creem una funció anomenada computepay que necessita dos inputs a i b.
def computepay(a, b):

    # En cas de fer hores extres.
    if float(a) > 40.0:

        # càlcul de les hores que es fan de més
        extrhr = float(a) - float (40.0)
        # preu/hora x 1.5 només per les hores extres
        extrrt = float(b) * float (1.5)
        # càlcul del salari sense tenir en compte hores extres
        SlrBs = (float(a) - extrhr) * float(b)
        # càlcul del salari extra
        Slrextr = float(extrhr) * float(extrrt)
        # suma sou 40 hores + sou hores extres
        Slr = SlrBs + Slrextr

        print ("Hores extres:", extrhr, "\n")
        print ("Sou extra:",Slrextr, "€\n")
        print ("Sou sense hores extra:", SlrBs, "€\n")

        #L'output de la funció serà el valor Slr (Salari base + extra)
        return Slr

    # En cas de no fer hores extres
    else:

    #Càlcul salari sense hores extre hores x preu/hora
        Slr = float(a) * float(b)

        #El return  en aquest cas tornarpa el valor Slr (Salari base sense hores extra)
        return Slr

# si els valors introduits son numerics (correcte) s'executa el codi
if thr > 0 and trt > 0:

# Aquest últim print mostra el sou total ja sigui amb hores extre o sense
#dins d'aquest print cridem a la funció amb els dos inputs inserits per l'usuari.
#Per tant s'imprimirà el valor que ens torni (return) la funció computepay.

    print("Sou total:", computepay(hr,rt), "€\n")

# Això s'executa en cas de que l'usuari no hagi introduit valors numérics

else:

     print ("Error! Uno de los valores introducidos no es numerico.")
