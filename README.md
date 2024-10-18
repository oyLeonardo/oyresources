<h1 align="center">
  <img src="https://raw.githubusercontent.com/oyLeonardo/oyresources/refs/heads/main/website/static/imgs/logositewhite.svg?token=GHSAT0AAAAAACYKEMU7IJ453474BCAIAXJUZYSNXTA" alt=oyresourceslogo width="500">
 <h4 align="center">Site pessoal para armazenamento de resourcepacks de Minecraft</h4>
</h1>

<p align="center">
  <a href="#features">Features </a> •
  <a href="#como-rodar">Como Rodar?</a> •
  <a href="#o-que-foi-usado">O Que Foi Usado</a> 
</p>

## Features

* Sistema de cadastro e login (email e senha não oficiais fucionam)
* Upload de imagem
  - Apenas imagens `.jpeg` são permitidas
  - As imagens são salvas em uma pasta `uploads` no backend
* Upload de arquivos
  - Apenas arquivos `.zip` são permitidos
  - Os arquivos são salvos em uma pasta `uploads` no backend
* Criação de posts  
* Edição de posts
* Edição de perfil
  - Email não pode ser alterado
* SUPER ADMIN (Controle dos posts e dos usuarios)

 > Como o projeto possui intuito pessoal, algumas funcionalidades podem conter problemas e/ou não conseguiram ter implementação completa. Esse foi meu primeiro projeto Orientado a Objetos e por isso decidi postá-lo no meu github

## Como Rodar?

```bash
# Clone esse repositorio
$ git clone https://github.com/oyLeonardo/oyresources.git

# Entre no repositorio
$ cd oyresources

# Criar o ambiente virtual
$ python -m venv .venv
# ou
$ python3 -m venv .venv

# Ativar o ambiente virtual

# Windows
$ .venv\Scripts\activate
# macOS e Linux
$ source .venv/bin/activate

# Instalar dependencias
$ pip install -r requirements.txt

# Rodar o projeto
$ python main.py
# ou
$ python3 main.py
```
> **Note**
> Se você está usando Linux Bash para o  Windows, [veja este guia](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) ou use o `node` do prompt de comando.

## O Que Foi Usado

Esse webapp usa as seguintes ferramentas/dependencias/pacotes:

- [Flask] (https://flask.palletsprojects.com/en/3.0.x/)
- [SQLAlchemy] &  [SQLite] 
 https://www.sqlalchemy.org/
