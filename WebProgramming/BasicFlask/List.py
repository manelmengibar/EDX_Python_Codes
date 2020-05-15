
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Manel", "Anna", "Neula", "Pau"]
    return render_template("index3.html", names=names)

if __name__ == "__main__":
    app.run(debug = True)
