from app import app
from flask import render_template

@app.route('/admin')
def index_admin():  #Funcion que anda cuando se está en "/"
    return render_template('/admin/admin_dashboard.html')

@app.route("/admin/stadistics")
def admin_stadistics():
    return "<h1 style='color:blue' > admin stadisticas </h1>"

