from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
login_manager = LoginManager()
UPLOAD_FOLDER = 'website/static/uploads/'
ALLOWED_EXTENSIONS = set(['jpg','png','jpeg']) #lista com formatos permitidos de imagem
def create_app():
    app = Flask(__name__) #criando objeto app com as funcionalidades do Flask
    app.config['SECRET_KEY'] = 'asdhaskdkashd' #configurando o site com uma secret key, importante mas ???
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(app.root_path, DB_NAME)}' #configurando onde vai ficar a nossa db , por conta de alteração na biblioteca flask fica essa feiura aqui pra aparecer database.db ali na esquerdinha
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    db.init_app(app) #iniciando app com as funcionalidades do SQLAlchemy
        
    from website.views import views
    from website.auth import auth
    
    app.register_blueprint(views,url_prefix = '/') #registrando nossas rotas
    app.register_blueprint(auth,url_prefix = '/') #registrando nossas rotas
    
    
    create_database(app)
    
    login_manager.login_view = 'auth.login' #configurando a rota de login
    login_manager.init_app(app)
    
    #agora colocar nossas rotas para funcionar e inserir coisas dos modelos
    return app   

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Database Criada!')
        
    
