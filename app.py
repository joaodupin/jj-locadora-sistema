
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuário fixo para login
USUARIO = "adminjj"
SENHA = "jard2149"

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    erro = ""
    if request.method == "POST":
        user = request.form["usuario"]
        senha = request.form["senha"]
        if user == USUARIO and senha == SENHA:
            return redirect("/painel")
        else:
            erro = "Usuário ou senha incorretos."
    return render_template("login.html", erro=erro)

@app.route("/painel")
def painel():
    return render_template("painel.html")
