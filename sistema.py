from flask import Flask, render_template, request, redirect, url_for
from funcao import adicionar_pessoa, listar_pessoas

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = int(request.form["idade"])
        adicionar_pessoa(nome, idade)
        return redirect(url_for("lista"))
    return render_template("index.html")

@app.route("/lista")
def lista():
    pessoas = listar_pessoas()
    return render_template("lista.html", pessoas=pessoas)

if __name__ == "__main__":
    app.run(debug=True)
