from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return usuario.query.get(user_id)

class usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 
    def json(self):
        return{
            'id':self.id,
            'email':self.email,
            'nome':self.nome,
            'senha':self.senha                             
        }    

class produto(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True)    
    nome = db.Column(db.String(255), nullable=True)
    tipo = db.Column(db.String(255), nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 

class contabilidade(db.Model):
    __tablename__ = "contabilidade"
    id = db.Column(db.Integer, primary_key=True)    
    fatura = db.Column(db.String(255), nullable=True)
    fiscal = db.Column(db.String(255), nullable=True)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())          


   