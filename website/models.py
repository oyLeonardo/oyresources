from . import db
from . import login_manager
from flask_login import UserMixin #serve para adicionar funcionalidades de login ao nosso modelo de usuário como is_active, is_authenticated, is_anonymous, get_id etc...
#criando modelos

class Usuario(db.Model,UserMixin): #criando a classe Usuario que herda de db.Model (classe do SQLAlchemy para criar modelos e usar na db)
    id = db.Column(db.Integer, primary_key=True) #criando a coluna id que é um inteiro e é a chave primária da tabela dos users
    nome = db.Column(db.String(150), nullable=False) #criando a coluna username que é uma string de até 150 caracteres, é a chave primária da tabela e não pode ser nula
    senha = db.Column(db.String(150), nullable=False) #criando a coluna senha que é uma string de até 150 caracteres e não pode ser nula
    email = db.Column(db.String(150), unique = True) #criando a coluna email que é uma string de até 150 caracteres, não pode ser nula e é 
    posts = db.relationship('Post',backref='usuario',lazy=True) #criando a relação entre a tabela usuario e a tabela post, onde um usuario pode ter vários posts
    is_admin = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean, default=True)  # Adicionando a coluna active

class Post(db.Model): #criando a classe Post que herda de db.Model (classe do SQLAlchemy para criar modelos e usar na db)
    id = db.Column(db.Integer,primary_key=True) #criando a coluna id que é um inteiro e é a chave primária da tabela
    titulo = db.Column(db.String(150), nullable=False) #criando a coluna titulo que é uma string de até 150 caracteres e não pode ser nula
    conteudo = db.Column(db.String(20000), nullable=False) #criando a coluna conteudo que é uma string de até 150 caracteres e não pode ser nula
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'),nullable=False) #criando a coluna usuario_id que é um inteiro e é uma chave estrangeira que referencia a coluna id da tabela usuario / ver print em Estudos/SQL
    data = db.Column(db.String(150)) #criando a coluna data que é um datetime e não pode ser nula, o default é a data e hora atual)
    imagens = db.relationship('Imagens',backref="post",lazy=True)
    arquivos = db.relationship('Arquivo',backref="post",uselist=False)
    
class Imagens(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String,nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),nullable = False)

class Arquivo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String,nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),nullable = False)
    
@login_manager.user_loader
def load_user(ident):
    return Usuario.query.get(int(ident))

    