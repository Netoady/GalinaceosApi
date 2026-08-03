from datetime import date
from helpers.application import app
from helpers.database import db

from models.Avicultor import Avicultor
from models.Endereco import Endereco
from models.Avicula import Avicula
from models.Galpao import Galpao
from models.Galinaceo import Galinaceo

def popular_banco():
    with app.app_context():
        try:
            print("Iniciando o povoamento com SQLAlchemy...")

            # 1. Instancia o Avicultor
            avicultor = Avicultor(
                nome="Chiquin Neto", 
                nascimento=date(1988, 1, 12), 
                cpf="12345678901", 
                caf="CAF123456"
            )
            db.session.add(avicultor)
            db.session.flush()  # Gera o id do avicultor sem fechar a transação

            # 2. Instancia o Endereço
            endereco = Endereco(
                logradouro="Rua dos Frango", 
                numero="100", 
                cep="58200000", 
                avicultor_id=avicultor.id
            )
            db.session.add(endereco)

            # 3. Instancia a Avícola
            avicula = Avicula(
                nome="Granja Ovo Feliz", 
                cnpj="12345678000195", 
                endereco="Sítio Galo Gago", 
                avicultor_id=avicultor.id
            )
            db.session.add(avicula)
            db.session.flush()  # Gera o id da avícola

            # 4. Instancia o Galpão
            galpao = Galpao(
                identificador="Galpão 01 - Poedeiras", 
                area_m2=500, 
                avicula_id=avicula.id
            )
            db.session.add(galpao)
            db.session.flush()  # Gera o id do galpão

            # 5. Instancia os Galináceos
            g1 = Galinaceo(
                sist_cria="1-SIST_POC", 
                niv_terr="UF", 
                cod_terr="25", 
                nom_terr="Paraíba", 
                cl_gal="01",
                galpao_id=galpao.id
            )
            db.session.add(g1)

            # Confirma todas as inserções no banco
            db.session.commit()
            print("Sucesso! Banco populado via SQLAlchemy ORM.")

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao popular o banco via ORM: {e}")

if __name__ == "__main__":
    popular_banco()