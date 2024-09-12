from website import create_app, db
from website.models import Post, Usuario, Imagens
from datetime import datetime
app = create_app()
now = datetime.now()
with app.app_context():
    if not Post.query.first():
        print("Criando Dummy...")
        data = now.strftime("%Y-%m-%d")
        new_dummy = Post(id = 1,titulo="teste",conteudo="opa",usuario_id=1,data = data)
        db.session.add(new_dummy)
        db.session.commit()
        print("Dummy Criado!")
    if not Usuario.query.filter_by(id=1).first():
        print("Criando admin")
        admin = Usuario(id = 1, nome = "admin",email = "admin@admin.com",senha = "admin",is_admin = True)
        db.session.add(admin)
        db.session.commit()
        
        print("Admin Criado!")
        
    if not Imagens.query.filter_by(filename='adminteste.png').first():
        print("Associando imagem teste ao post teste")
        imagemteste = Imagens(id = 1, filename = "adminteste.png",post_id = 1)
        db.session.add(imagemteste)
        db.session.commit()
        print("Imagem Associada!")
           

if __name__ == '__main__':
    app.run(debug = True)
    