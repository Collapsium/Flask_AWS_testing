from app import app
from flask import render_template, request, redirect
from rds import connection

@app.route('/')
def index():  #Funcion que anda cuando se está en "/"
    return render_template('/public/index.html')

@app.route("/data")
def data():
    dato = "amongus" #Puede ser cualquier objeto de python
    arr_data = ["dato1 de arr", "dato2 de arr", "dato3 de arr"]
    dict_data = {"dato1 de dictionary": 1, "dato2 de dictionary": 2, "dato3 de dictionary": 3}
    pool_data = ("pool1", "pool2")

    def funcion(x, qty):
        return x * qty

    class clase_epica:
        def __init__(self, arg):
            self.arg = arg

        def test(self):
            return f"funcionando clase_epica, {self.arg}"

    my_clase_epica = clase_epica(
        arg = "amongus"
    )

    return render_template(
        '/public/data.html',
        dato=dato,
        arr_data = arr_data,
        dict_data = dict_data,
        pool_data = pool_data,
        clase_epica = clase_epica,
        my_clase_epica = my_clase_epica
    )

@app.route("/recommendations")
def recommendations():
    #pasarle la bd?

    data = connection.getRecommendations()
    return render_template('/public/recommendations.html',
                           data =   data
                           )

@app.route("/add" ,methods=["GET", "POST"]) #Get está definido por defecto
def add():

    if request.method == "POST":
        r = request.form

        #Sacado de names en add.html
        username = r["username"]
        url = r["url"]
        description = r["description"]

        connection.addRecommendation([username,url,description])

    return render_template('/public/add.html',
                           connection =connection
                           )