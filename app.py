#Importando módulos necessários para a aplicação Flask 
from flask import Flask, render_template #Importando classe Flask e Render_Template do módulo flask
from flask_sqlalchemy import SQLAlchemy #Importando SQLAlchemy do módulo flask_sqlalchemy

#Criando a aplicação Flask
app = Flask(__name__) #Criando aplicação Flask

#Rotas da aplicação
@app.route("/") #Define rota principal
def index(): #Função para página principal
    return render_template("index.html") #Retorno da função index, retorna HTML da página principal

@app.route("/planos") #Define rota para página de planos
def planos(): #Função para página de planos
    return render_template("planos.html") #Retorno da função planos, retorna HTML da página de planos

@app.route("/agenda") #Define rota para página de agenda
def agenda(): #Função para página de agendamento
    return render_template("agendamento.html") #Retorno da função agenda, retorna HTML da página de agendamento

@app.route("/profissionais") #Define rota para página de profissionais
def profissionais():#Função para página de profissionais
    return render_template("profissionais.html")#Retorno da função profissionais, retorna HTML da página de profissionais

@app.route("/login") #Define rota para página de login
def login(): #Função para página de login
    return render_template("login.html") #Retorno da função login, retorna HTML da página de login

#Back-End
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/bladesys' #Configuração do banco de dados SQLite
db = SQLAlchemy(app) #Criação do objeto de banco de dados
#Criando Tabelas do banco de dados
#class

#Modo Depuração 
if __name__ == "__main__": #Compara se a aplicação criada é a principal
    app.run(debug=True) #Inicia servidor em modo de depuração (a cada alteração o servidor atualiza)