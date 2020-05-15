# Aplicació que ens deixa afegir passastgers als vols que tenim a la taula "flights"
# Interactua amb les taules de "flights" per consultar i amb la de "passengers" per afegir-hi dades.
#Les taules "flights" i "passengers" han estat creades anteriorment amb sql
#Mitjançant la llibreria flask utilitzem plantilles html (dins de SqlFlask>templates)
#que ens permeten interactuar amb el codi mitjançant una URL donada.




from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

#instruccions per interactuar amb la base de dades
engine = create_engine("postgresql://localhost/python")
db = scoped_session(sessionmaker(bind=engine))

#pàgina principal
@app.route("/")
def index():
    #Agafa tots els valors de la taula "flights"
    flights = db.execute("SELECT * FROM flights").fetchall()
    #Consultar fitxer "index.html" per veure que se'ns mostrarà a la URL.
    return render_template("index.html", flights=flights)

#apartat per fer reserves
@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    #Valor que introduirem referent a la persona que vol reservar el vol
    name = request.form.get("name")

    #Control en cas de proporcionar un id no admés.
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    #If per controlar que seleccionem un vol.
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id.")
    #En cas de ser tot correcte procedim a inserir el passatger a la taula passengers.
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    {"name":name, "flight_id": flight_id})

    #Hem d'indicar això per a que es guardin les accions que hem realitzat.
    db.commit()
    #Consultar fitxer "success.html"per veure que es mostrarà
    return render_template("success.html")



if __name__ == "__main__":
    app.run(debug = True)
