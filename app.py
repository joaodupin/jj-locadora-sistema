
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bem-vindo à JJ Locadora de Veículos</h1>"
