from .datacontroller import Datacontroller
from flask_login import current_user,login_user
from flask import redirect,url_for,flash,jsonify

datactl = Datacontroller()


class Appcontroller():
    def ehadmin(self):
        '''verifica se o admin existe e é o que ta tentando acessar, se sim retorna todos os users e posts'''
        if datactl.check_existe() == True:
            if current_user.is_admin == False:
                print("não é adm")
                return False
            else:
                print("é adm")
                return True
        else:
            print("adm nao encontrado no banco de dados")
            return redirect(url_for("views.home"))
    
    def authenticate_user(self,emaillogin,senhalogin):
        '''recebe email e senha, se achar: loga user e retorna a página home, se não retorna pagina login'''
        user_existe = datactl.procurar_email(emaillogin)
        if user_existe:
            print("email encontrado")
            password = datactl.procurar_senha(senhalogin)
            if password:
                print("senha certa")
                user = datactl.get_Usuario_Id(emaillogin).first()
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Usuario ou senha incorretos")
                return redirect(url_for('auth.login'))
        else:
            flash("Usuario ou senha incorretos")
            return redirect(url_for('auth.login'))
    
    def registrar_user(self,email1,email2,senha1,senha2,nome):
        if len(nome) < 2:
            flash("Erro, nome muito curto.")
            return redirect(url_for('auth.signin'))
        elif len(nome) > 20:
            flash("Erro, nome muito longo.")
            return redirect(url_for('auth.signin'))
        elif len(email1) < 4:
            flash("Erro, email muito curto.")
            return redirect(url_for('auth.signin'))
        elif email1 != email2:
            flash("Erro, emails diferentes.")
            return redirect(url_for('auth.signin'))
        elif len(senha1) < 5:
            flash("Erro, senha muito curta.")
            return redirect(url_for('auth.signin'))
        elif senha1 != senha2:
            flash("Erro, senhas diferentes.")
            return redirect(url_for('auth.signin'))
        elif datactl.procurar_email(email1) == True:
            flash("Erro, email já cadastrado!")  
            return redirect(url_for('auth.signin'))
        elif datactl.procurar_nome(nome) == True:
            flash("Erro, nome já está sendo usado")
            return redirect(url_for('auth.signin'))
        else:
            print("tudo certo")
            flash("Usuário registrado com sucesso!")
            datactl.create_user(nome,email1,senha1)
            return redirect(url_for('auth.login'))
        
    def create_post(self,titulo,conteudo,filename,zip):
        new_post = datactl.create_conteudo(titulo=titulo,conteudo=conteudo)
        datactl.create_img(filename=filename,post_id=new_post.id)
        datactl.create_zip(filename=zip.filename,post_id=new_post.id)
        
    def create_zip(self,zip,post_id):
        filename = zip.filename
        post_id = post_id
        datactl.create_zip
        
    def deletar_user(self,user,userId):
        user = datactl.get_Usuario_by_Id(userId)
        if user:
            print("entrou if")
            datactl.deleteuser(user)
            print("deletou")
        return jsonify({})
    
    def deletar_post(self,post,postId):
        print("apt")
        post = datactl.get_Post_by_id(postId)
        imagempost = datactl.get_Imagem_by_post_id(postId)
        arquivopost = datactl.get_Arquivo_by_post_id(postId)
        if post:
            print("tem post?:",post)
            print("tem imagem?:",imagempost)
            print("tem arquivo?:",arquivopost)
            print("deletando post inteiro")
            datactl.deleteimagem(imagempost)
            datactl.deletearquivo(arquivopost)
            datactl.deletepost(post)
            
            print("deletou tudo")
        return jsonify({})
    
    def atualizar_user(self,new_nome,new_senha1,new_senha2,user_id):
        print("entrou atualizar_user")
        print(new_nome)
        if new_nome != None:
            print("nome entrou")
            if len(new_nome) < 2:
                flash("Erro, nome muito curto.")
            elif len(new_nome) > 20:
                flash("Erro, nome muito longo.")
            elif datactl.procurar_nome(new_nome) == True:
                flash("Erro, nome já está sendo usado")
            else:
                datactl.atualizar_user_nome(new_nome,user_id)
                flash("As alterações foram salvas!")
                return redirect(url_for("views.perfil"))
        if (new_senha1 and new_senha2) != None:
            if len(new_senha1) < 5:
                flash("Erro, senha muito curta.")
            elif new_senha1 != new_senha2:
                flash("Erro, senhas diferentes.") 
            else:
                datactl.atualizar_user_senha(new_senha1,user_id)
                flash("As alterações foram salvas!")
                return redirect(url_for("views.perfil"))
        else:
            flash("Nenhuma alteração feita.")
            return redirect(url_for("views.perfil"))
    
    def atualizar_post(self,newtitulo,newconteudo,newpost_id):
        print("entrou atualizar post")
        print(newtitulo)
        print(newconteudo)
        print(newpost_id)
        if newtitulo != newpost_id.titulo:
            datactl.atualizar_post_titulo(newtitulo,newpost_id.id)
            print("voltou")
            flash("As alterações foram salvas!")
            return redirect(url_for("views.pagina_post",titulo=newtitulo))
        elif newconteudo != newpost_id.conteudo:
            datactl.atualizar_post_conteudo(newconteudo,newpost_id.id)
            flash("As alterações foram salvas!")
            return redirect(url_for("views.pagina_post",titulo=newtitulo))
        else:
            flash("Nenhuma alteração feita.")
            
        
    
        
        
        