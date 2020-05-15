

from datetime import date

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():


    now = date.today()
    duedate = date(2020, 10, 21)

    days = (duedate - now)

    return render_template("index2.html", days = days.days)



if __name__ == "__main__":
    app.run(debug = True)
