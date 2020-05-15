

#importamos flask del módulo flask que alguien ha desarollado antes.
from flask import Flask

#Esto indica que quiero aplicar una aplicación web utilizando Flask
app = Flask(__name__)


# Esto indica que cuando se introduce / en el buscador se accede a la función que viene a continuación
@app.route("/")

# Ejecutamos la función index de python y devolvemos un mensaje simple
def index():
    return "Hello, World!"


#Esto permite introducir el nombre que queramos en la url.
@app.route("/<string:name>")

def hello(name):
    name = name.capitalize() # devolverá el nombre con la primera letra en mayúsculas
    return f"<h1>Hello, {name}!<h>" #Utilizando <h1> haremos que esto se muestre en negrita y más grande


if __name__ == "__main__":
    app.run(debug = True)
