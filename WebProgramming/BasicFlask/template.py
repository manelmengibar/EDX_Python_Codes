
#importamos flask del módulo flask que alguien ha desarollado antes.
#En este caso importamos también la función render_template que se encuentra dentro de Flask
from flask import Flask, render_template

#Esto indica que quiero crear una aplicación web utilizando Flask
app = Flask(__name__)


# Esto indica que cuando se introduce / en el buscador se accede a la función que viene a continuación
@app.route("/")

def index():

    #Con esta variable puedo variar el mensaje que se mostrará en la cabezera de mi página sin modificar la plantilla html
    headline = "Hello!"

    #En este caso hace un return de una plantilla con formato html que se encuentra dentro de una carpeta
    #llamada "templates" (siempre buscara una carpeta en la misma ubicación del código actual y con esta nomenclatura)
    #y buscará el fichero dentro de esta carpeta con el nombre que indiquemos y con la extensión html
    #El formato y la información de la página web se editaran en el fichero con extensión html.
    #Este código solo llamará a la plantilla html.
    #Una vez en la página web podemos hacer botón derecho "View Page source" veremos el código en html de nuestra página
    return render_template("index.html", headline=headline)

#Si a nuestra dirección añadimos "/bye" se ejecutará lo que viene a continuación
@app.route("/bye")

def bye():
    #headline es la variable que podemos modificar con la misma plantilla index.html
    headline = "See ya!"
    return render_template("index.html", headline=headline)



if __name__ == "__main__":
    app.run(debug = True)
