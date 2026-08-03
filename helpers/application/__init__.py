import os
from flask import Flask
from flask_restful import Api
from helpers.database import db, close_connection


app = Flask(__name__)
api = Api(app)

# Configura a URI do banco (puxando do .env ou usando a string direta)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'postgresql://postgres:123456@localhost:5435/galinaceos'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy com as configurações carregadas
db.init_app(app)
app.teardown_appcontext(close_connection)  # Fecha a conexão com o banco ao final de cada requisição