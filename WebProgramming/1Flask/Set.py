
#set es una función que crea un conjunto donde almacenar elementos
s = set()

#dentro de este set podemos ir añadiendo elementos sin orden
s.add(1)
s.add(3)
s.add(5)
s.add(3)

#Este print mostrará: {1, 3, 5}. Como podemos ver solo muestra una vez el 3
#ya que lo que importa es el elemento que hay y no cuantas veces está
print(s)
     
