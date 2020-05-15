
from flask import Flask, render_template

app = Flask(__name__)

#En aquest cas cridem a un template html.
@app.route("/")
def index():
    headline = "Benvinguts a la meva pàgina web"
    return render_template("index.html", headline = headline)

#En aquest cas cridem a un altre template html.
@app.route("/familia")
def familia():
    names = ["Manel", "Anna", "Neula", "Pau"]
    return render_template("index3.html", names = names)

if __name__ == "__main__":
    app.run(debug = True)
