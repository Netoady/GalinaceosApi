from helpers.application import app
from helpers.database import db
from helpers.logger import logger

from models.Avicultor import Avicultor
from models.Endereco import Endereco
from models.Avicula import Avicula
from models.Galpao import Galpao
from models.Galinaceo import Galinaceo

def inicializar_banco():
  with app.app_context():
    try:

      print("Iniciando a criação do schema do banco de dados com SQLAlchemy...")
      db.drop_all()  # Remove todas as tabelas existentes
      db.create_all()
      print("Schema do banco de dados criado com sucesso!")
    except Exception as err:
      logger.error(f"Erro ao criar o schema do banco de dados: {err}")

        
      
if __name__ == "__main__":
  inicializar_banco()