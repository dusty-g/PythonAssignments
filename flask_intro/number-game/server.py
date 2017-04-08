from flask import Flask, redirect, request, session, render_template
from random import randint
app = Flask(__name__)
app.secret_key = 'a112swefdsdas'


@app.route("/")
def start():
    if "number" in session:
        return render_template("index.html", visibility = "hidden", hint= "hidden")
    else:
        session["number"] = randint(1, 100)
        print session["number"]
        return render_template("index.html", visibility = "hidden", hint = "hidden")
@app.route("/check", methods=["POST"])
def check():
    session["guess"] = int(request.form['guess'])
    if session["guess"] == session["number"]:
        print "session guess:", session["guess"]
        print "session number:", session["number"]
        return render_template("index.html", visibility = "correct", hint = "hidden")
    elif session["guess"] > session["number"]:
        print "high"
        print "session guess:", session["guess"]
        print "session number:", session["number"]
        return render_template("index.html", visibility= "hidden", hint = "high")
    else:
        print "low"
        return render_template("index.html", visibility = "hidden", hint = "low")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")
app.run(debug=True)