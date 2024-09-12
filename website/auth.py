from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import login_required,logout_user,current_user
from .controllers.appcontroller import Appcontroller

appctl = Appcontroller()

auth = Blueprint('auth', __name__)

@auth.route('/login',methods = ['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        emaillogin = request.form.get('email')
        senhalogin = request.form.get('senha')
        result = appctl.authenticate_user(emaillogin,senhalogin)
        return result
        
@auth.route('/signin',methods = ['POST','GET'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == 'POST':
        email1 = request.form.get('email1')
        email2 = request.form.get('email2') 
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        nome = request.form.get('nome')
        appctl.registrar_user(email1,email2,senha1,senha2,nome)
        return redirect(url_for("auth.login"))
    return render_template("signin.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    