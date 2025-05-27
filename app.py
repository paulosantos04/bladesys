from flask import Flask, render_template #Importando classe Flask e Render_Template do módulo flask
 
app = Flask(__name__) #Criando aplicação Flask

@app.route("/") #Define rota principal
def login(): #Função ára página de login
    return render_template("login.html") #Retorno da função login, retorna HTML da página de login

@app.route("/planos") #Define rota para página de planos
def planos(): #Função para página de planos
    return render_template("planos.html") #Retorno da função planos, retorna HTML da página de planos

@app.route("/agenda") #Define rota para página de agenda
def agenda(): #Função para página de agendamento
    return render_template("agendamento.html") #Retorno da função agenda, retorna HTML da página de agendamento

@app.route("/cadastro") #Define rota para página de cadastro
def cadastro(): #Função para página de cadastro
    return render_template("cadastro.html") #Retorno da função cadastro, retorna HTML da página de cadastro

#@app.route("/login") #Define rota para página de login
#def login(): #Função para página de login
    #return render_template("login.html") #Retorno da função login, retorna HTML da página de login

if __name__ == "__main__": #Compara se a aplicação criada é a principal
    app.run(debug=True) #Inicia servidor em modo de depuração (a cada alteração o servidor atualiza)