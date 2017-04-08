from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
# @app.route("/result")
# def result():
#     return render_template("result.html")
@app.route("/submit", methods=["POST"])
def submit():
    name1 = request.form["name"]
    location1 = request.form["location"]
    language1 = request.form["language"]
    comment1 = request.form["comment"]
    # return render_template("result.html", name= name, location=location, language=language, comment=comment)
    return render_template("result.html", name = name1, location = location1, language=language1, comment=comment1)
app.run(debug=True)
    