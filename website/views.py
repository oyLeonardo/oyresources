from flask import Blueprint,render_template,request,redirect,url_for,flash,current_app,abort,send_from_directory
from flask_login import login_required,current_user
from website.controllers.datacontroller import Datacontroller
from website.controllers.appcontroller import Appcontroller
from werkzeug.utils import secure_filename
from . import ALLOWED_EXTENSIONS
import os, json

views = Blueprint('views',__name__)
datactl = Datacontroller()
appctl = Appcontroller()

@views.route("/",methods=["POST","GET"])
def home():
    posts = datactl.get_Posts()
    imagens = datactl.get_Imagens()
    if request.method == "POST":
        return redirect(url_for("views.home"))
    else:
        return render_template("home.html",imagens=imagens, current_user = current_user, allposts = posts)

@views.route("db",methods = ["GET","POST"])
@login_required
def db_view():
    if appctl.ehadmin():
        posts = datactl.get_Posts()
        users = datactl.get_Usuario()
        print(users)
        print(posts)
        return render_template("db.html",users = users,posts = posts) 
    else:
        abort(404)

@views.route("postar",methods = ["GET","POST"])
@login_required
def postar():
    if request.method == "POST":
        img = request.files["file"]
        zip = request.files["zip"]
        
        if 'zip' not in request.files:
            flash('No file part')
            return redirect(url_for("views.postar"))

        if zip.filename == '':
            flash('No selected file')
            return redirect(url_for("views.postar"))
        
        if datactl.check_Imagem_nome(img.filename):
            name, ext = os.path.splitext(img.filename)
            img.filename = f"{name}1{ext}"
            
        if datactl.check_Zip_nome(zip.filename):
            name, ext = os.path.splitext(zip.filename)
            zip.filename = f"{name}1{ext}"
        
        if 'file' not in request.files:
            flash('No file')
            return redirect(url_for("views.postar"))
        
        if img.filename == '':
            flash('no image or file selected')
            return redirect(url_for("views.postar"))
        
        if (img and allowed_file(img.filename)) and (zip and zip.filename.endswith('.zip')):
            filename = secure_filename(img.filename)
            titulo = request.form.get("titulo")
            conteudo = request.form.get("conteudo")
            appctl.create_post(titulo,conteudo,filename,zip)
            img.seek(0)
            img.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))
            zip.save(os.path.join(current_app.config['UPLOAD_FOLDER'],zip.filename))
            return redirect(url_for("views.home"))
        else:
            flash('')
            return redirect(url_for("views.postar")) 
    else:
        return render_template("post.html")

@views.route("/perfil",methods=["GET","POST"])
@login_required
def perfil():
    if request.method == "GET":
        userposts = datactl.get_user_Posts(current_user)
        imagens = datactl.get_Imagens()
        user = current_user
        return render_template("perfil.html",userposts = userposts,imagens = imagens,user = user)
    if request.method == "POST":
        print("entrou postmethod")
        new_nome = request.form.get("newnome")
        print(new_nome)
        new_senha1 = request.form.get("newsenha1")
        new_senha2 = request.form.get("newsenha2")
        appctl.atualizar_user(new_nome,new_senha1,new_senha2,current_user.id)
        
        return redirect(url_for("views.perfil"))

@views.route("/<titulo>",methods = ["GET"])
def pagina_post(titulo):
    post = datactl.get_Post_by_title(titulo)
    if post:
        return render_template("postpagina.html",post = post)   
    else:
        abort(404)
        
    
def allowed_file(img):
    '''transforma tudo depois do . no formato do arquivo em string e verifica se oq foi transformado ta na lista ALLOWED_EXTENSIONS'''
    return '.' in img and img.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@views.route("/deleteuser", methods=["POST"])
@login_required
def delete_user():
    print("delete-user")
    user = json.loads(request.data)
    userId = user["userId"]
    flash("conta deletada com sucesso!")
    return appctl.deletar_user(user,userId)

@views.route("/deletepost", methods=["POST"])
@login_required
def delete_post():
    print("delete-post")
    post = json.loads(request.data)
    print(post)
    postId = post["postId"]
    return appctl.deletar_post(post,postId)

@views.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static/uploads', filename)

@views.route("/postedit/<titulo>",methods=["GET","POST"])
@login_required
def postedit(titulo):
    post = datactl.get_Post_by_title(titulo)
    if request.method=="GET":
        print(post)
        imagem = datactl.get_Imagem_by_post_id(post.id)
        print("entrou get post")
        if post:
            print(post)
            return render_template("postedit.html",post = post,imagem = imagem)   
        else:
            abort(404)
    if request.method == "POST":
        post = datactl.get_Post_by_title(titulo)
        print(post)
        print("entrou postmethod")
        new_titulo = request.form.get("newtitulo")
        print(new_titulo)
        new_conteudo = request.form.get("newconteudo")
        print(new_conteudo)
        print(post)
        appctl.atualizar_post(new_titulo,new_conteudo,post)
        return redirect(url_for("views.pagina_post",titulo=new_titulo))
    