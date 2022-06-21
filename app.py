from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/indexx.html")
def indexx():
    return render_template("indexx.html")

@app.route("/contatos.html")
def contatos():
    return render_template("contatos.html")

@app.route("/projetos.html")
def projetos():
    return render_template("projetos.html")

