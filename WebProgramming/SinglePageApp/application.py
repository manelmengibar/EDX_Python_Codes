
 from flask import Flask, render_template

 app = Flask(__name__)

 @app.route("/")
 def index():
     return render_template("index.html")


texts = ["This is the first text",
        "This is the second text",
        "This is the third text"]

@app.route("/first")
def first():
    returns texts[0]

@app.route("/second")
def first():
    returns texts[1]

@app.route("/third")
def first():
    returns texts[2]

if __name__ == "__main__":
    app.run(debug=True)
