from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    name = "M sindhuja"
    return render_template("sindhuja.html",name=name)

@app.route("/work")
def my_work():
    return "I am working at Springml"
app.run()