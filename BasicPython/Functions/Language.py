
#Creem la funció 'greet' que imprimeix una cosa o una altra (output)
#en funció de l'input que li donem.
def greet(lang):

    if lang == "es":

         print ("Has seleccionado español.\n")

    elif lang== "cat":

        print ("Has escollit català.\n")

    else:

        print ("Wrong format! You must type 'es' or 'cat'.\n")


#Demanem un input al usuari.
x = input ("choose a language\n")

#Cridem a la funció 'greet' que hem creat abans i li donem com a input el que ha introduit l'usuari.
greet (x)
