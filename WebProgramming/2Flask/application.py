

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    headline = "Benvinguts a la nostra pàgina web"
    text = " De moment no tenim gaire contingut, I KNOOOOW!"
    #En aquest cas cridem a un template html.
    return render_template("index.html", headline = headline, text = text)


@app.route("/familia")
def more():
    names = ["Manel", "Anna", "Neula", "Pau...Downloading"]
    #En aquest cas cridem a un altre template html.
    return render_template("more.html", names = names)

if __name__ == "__main__":
    app.run(debug = True)
