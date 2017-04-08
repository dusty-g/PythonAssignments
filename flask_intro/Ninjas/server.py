from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninjas/")
def default():
    return render_template("ninjas.html", variable = "ninja")
@app.route("/ninjas/<color>")
def ninja(color):
    print color
    if color == "blue":
        return render_template("ninjas.html", variable = "blue")
    elif color == "purple":
        return render_template("ninjas.html", variable = "purple")
    elif color == "red":
        return render_template("ninjas.html", variable = "red")
    elif color == "orange":
        return render_template("ninjas.html", variable = "orange")
    else:
        
        return render_template("ninjas.html", variable = "april")
    
app.run(debug=True)