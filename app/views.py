from app import app
from flask import render_template

@app.route('/')
def index():  #Funcion que anda cuando se está en "/"
    return render_template('/public/index.html')

@app.route("/pagina2")
def pagina2():
    return "<h1 style='color:blue' > pagina2 </h1>"
