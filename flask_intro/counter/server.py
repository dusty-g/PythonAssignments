from flask import Flask, redirect, request, session, render_template
app = Flask(__name__)
app.secret_key = 'ougyuyg'

@app.route("/")
def index():
    print session
    
    if "count" in session:
        session["count"] = session["count"] + 1
        return render_template("index.html")
    else:
        session["count"] = 1
        return render_template("index.html")
@app.route("/two")
def two():
    session["count"] = session["count"] + 1
    return redirect("/")

@app.route("/reset")
def reset():
    session["count"] = 0
    return redirect("/")


app.run(debug=True)