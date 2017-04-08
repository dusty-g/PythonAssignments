from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = "3122a12"

def getGold(a, b):
    
    activityString = "Earned "
    amount = randint(a, b)
    session["gold"] = session["gold"] + amount
    activityString += str(amount)
    activityString += " from the " + request.form["building"]
    session["activities"].append(activityString)
    print session["activities"]
    return render_template("index.html", gold = session["gold"])


@app.route("/")
def index():
    if "gold" in session:
        print "there's a session already"
        return render_template("index.html", gold = session["gold"])
    else:
        session["gold"] = 0
        session["activities"] = []
        return render_template("index.html", gold = session["gold"])

@app.route("/process", methods=['POST'])
def process():
    if request.form["building"] == "cave":
        return getGold(5,10)
    elif request.form["building"] == "farm":
        print "farm!"
        return getGold(10, 20)
    elif request.form["building"] == "house":
        return getGold(2,5)
    elif request.form["building"] == "casino":
        return getGold(-50, 50)
    else:
        return redirect("/")

@app.route("/reset", methods=["Post"])
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)