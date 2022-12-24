from flask import Flask

#lo que traeremos a flask, por el nombre python cacha que es un package

app = Flask(__name__, template_folder='../templates')
from app import views
from app import admin_views
