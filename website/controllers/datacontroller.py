from website.models import Usuario,Post,Imagens,Arquivo
from datetime import datetime
from flask_login import current_user
from website import db
import os
now = datetime.now()
class Datacontroller:
    def create_conteudo(self,titulo,conteudo):
        '''recebe titulo e conteudo, cria um post com o id do current user'''
        data =  now.strftime("%Y-%m-%d")
        new_post = Post(titulo = titulo,conteudo = conteudo,data = data,usuario_id = current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return new_post
        
    def create_user(self,nome,email1,senha1):
        novo_usuario = Usuario(nome = nome,email = email1,senha = senha1,is_admin = False)   
        db.session.add(novo_usuario)
        db.session.commit() 
        
    def check_existe(self):
        '''verifica se o admin (is_admin = 1) existe no banco de dados'''
        if Usuario.query.filter_by(is_admin = 1).first():
            return True
        else:
            return False
    
    def get_Usuario(self):
        '''retorna todos os users do model'''
        users = Usuario.query.all()
        return users
    
    def get_Usuario_Id(self,variavel):
        '''insere variavel email ou nome e retorna id do user na db'''
        user_id = Usuario.query.filter((Usuario.email == variavel) | (Usuario.nome == variavel))
        return user_id
        
    
    def get_Posts(self):
        '''retorna todos os posts do model'''
        posts = Post.query.all()
        return posts
    
    def get_Post_by_title(self,titulo):
        '''retorna o post do model com o titulo fornecido'''
        post = Post.query.filter_by(titulo = titulo).first()
        return post
    
    def get_Post_by_id(self,id):
        '''retorna o post do model com o titulo fornecido'''
        post = Post.query.filter_by(id = id).first()
        return post
    
    def get_Post_id(self):
        post_id = Post.query.order_by(Post.date_created.desc()).first()
        return post_id
    
    def get_Imagem_by_post_id(self,id):
        imagem = Imagens.query.filter_by(id = id).first()
        return imagem
    
    def get_Imagens(self):
        imagens = Imagens.query.all()
        return imagens
    
    def check_Imagem_nome(self,filename):
        if Imagens.query.filter_by(filename = filename).first() == None:
            return False 
        else:
            return True       
    
    def check_Zip_nome(self,filename):
        if Arquivo.query.filter_by(filename = filename).first() == None:
            return False 
        else:
            return True  
    
    def procurar_email(self,emaillogin):
        '''Função que procura um email no banco de dados, coloca email se existir retorna True se não, retorna False'''
        resultado = Usuario.query.filter_by(email=emaillogin).first()
        if resultado == None:
            return False
        else:
            return True
    
    def procurar_senha(self,senhalogin):
        '''Função que procura uma senha no banco de dados, coloca senha se existir retorna True se não, retorna False'''
        resultado = Usuario.query.filter_by(senha=senhalogin).first()
        if resultado == None:
            return False
        else:
            return True
        
    def procurar_nome(self,nome):
        '''Função que procura um nome no banco de dados, coloca nome se existir retorna True se não, retorna False'''
        resultado = Usuario.query.filter_by(nome=nome).first()
        if resultado == None:
            return False
        else:
            return True
    
    def create_img(self,filename,post_id):
        '''cria imagem com bytes(imagem em si) nome e tipo'''
        filename = filename
        new_image = Imagens(filename=filename,post_id=post_id)
        db.session.add(new_image)
        db.session.commit()
    
    def get_user_Posts(self,current_user):
        posts = Post.query.filter_by(usuario_id = current_user.id).all()
        return posts
    
    def get_Usuario_by_Id(self,id):
        return Usuario.query.filter_by(id = id).first()
        
    def deleteuser(self,userid):
        print("deletando usuario")
        print(userid)
        db.session.delete(userid)
        db.session.commit()
        print("usuario deletado")
        
    def deletepost(self,post):
        if post:
            print("deletando post")
            print(post)
            db.session.delete(post)
            db.session.delete
            db.session.commit()
            print("post deletado")
        else:
            return print("não tem post")    
    
    def deleteimagem(self,imagem):
        if imagem:
            print("deletando imagem")
            print(imagem)
            db.session.delete(imagem)
            db.session.delete
            db.session.commit()
            filepath = os.path.join('website/static/uploads', imagem.filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"imagem deletada com sucesso")
            else:
                print(f"imagem não encontrada")
        else:
            return print("não tem imagem") 
    
    def deletearquivo(self,arquivo):
        if arquivo:
            print("deletando arquivo")
            print(arquivo)
            db.session.delete(arquivo)
            db.session.commit()
            print("arquivo deletado") 
            filepath = os.path.join('website/static/uploads', arquivo.filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"arquivo deletado com sucesso")
            else:
                print(f"aqruivo não encontrado")
        else:
            return print("não tem arquivo")
    
    def create_zip(self,filename,post_id):
        new_zip = Arquivo(filename=filename,post_id=post_id)
        db.session.add(new_zip)
        db.session.commit()
    
    def get_Arquivo_by_post_id(self,postId):
        zip = Arquivo.query.filter_by(post_id=postId).first()
        return zip
    
    def atualizar_user_nome(self,new_nome,user_id):
        print("atualizando nome do usuario")
        user = Usuario.query.filter_by(id=user_id).first()
        user.nome = new_nome
        db.session.add(user)
        db.session.commit()
        print("nome do usuario atualizado")
        
    def atualizar_user_senha(self,new_senha,user_id):
        print("atualizando senha do usuario")
        user = Usuario.query.filter_by(id=user_id).first()
        user.senha = new_senha
        db.session.add(user)
        db.session.commit()
        print("senha do usuario atualizada")
    
    def atualizar_post_conteudo(self,newconteudo,post_id):
        print("atualizando conteudo do post")
        post = Post.query.filter_by(id=post_id).first()
        post.conteudo = newconteudo
        db.session.add(post)
        db.session.commit()
        print("conteudo do post atualizado")
    
    def atualizar_post_titulo(self,newtitulo,post_id):
        print("atualizando titulo do post")
        post = Post.query.filter_by(id=post_id).first()
        post.titulo = newtitulo
        db.session.add(post)
        db.session.commit()
        return print("titulo do post atualizado")
    
    def atualizar_post_img(self,newimg,post_id):
        print("atualizando imagem do post")
        post = Post.query.filter_by(id=post_id).first()
        post.conteudo = newimg
        db.session.add(post)
        db.session.commit()
        print("imagem do post atualizado")
    
    def atualizar_post_zip(self,newzip,post_id):
        print("atualizando zip do post")
        post = Post.query.filter_by(id=post_id).first()
        post.conteudo = newzip
        db.session.add(post)
        db.session.commit()
        print("zip do post atualizado")
    