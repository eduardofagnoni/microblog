from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    nome = 'Eduardo Fagnoni'
    dados = {'profissao':'Programador', 'nome':'Eduardo', 'sobrenome':'Fagnoni'}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
