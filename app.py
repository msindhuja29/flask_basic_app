from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    name = "sindhuja M"
    return render_template("sindhuja.html",name=name)



app.run()