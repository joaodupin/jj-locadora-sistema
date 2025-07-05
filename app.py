
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("locadora.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS veiculos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            modelo TEXT, placa TEXT, ano INTEGER, diaria REAL, mensal REAL
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT, telefone TEXT, documento TEXT
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS locacoes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cliente_id INTEGER, veiculo_id INTEGER,
                            data_inicio TEXT, data_fim TEXT, valor REAL
                        )''')

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["usuario"] == "adminjj" and request.form["senha"] == "jard2149":
            return redirect("/painel")
    return render_template("login.html")

@app.route("/painel")
def painel():
    return render_template("painel.html")

@app.route("/veiculos", methods=["GET", "POST"])
def veiculos():
    if request.method == "POST":
        modelo = request.form["modelo"]
        placa = request.form["placa"]
        ano = request.form["ano"]
        diaria = request.form["diaria"]
        mensal = request.form["mensal"]
        with sqlite3.connect("locadora.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO veiculos (modelo, placa, ano, diaria, mensal) VALUES (?, ?, ?, ?, ?)",
                           (modelo, placa, ano, diaria, mensal))
        return redirect("/veiculos")
    with sqlite3.connect("locadora.db") as conn:
        cursor = conn.cursor()
        veiculos = cursor.execute("SELECT * FROM veiculos").fetchall()
    return render_template("veiculos.html", veiculos=veiculos)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
