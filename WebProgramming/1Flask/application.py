
#importamos flask del módulo flask que alguien ha desarollado antes.
from flask import Flask

#Esto indica que quiero aplicar una aplicación web utilizando Flask
app = Flask(__name__)

# Esto indica que cuando se introduce / en el buscador se accede a la función que viene a continuación
@app.route("/")

# Ejecutamos la función index de python y devolvemos un mensaje simple
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
