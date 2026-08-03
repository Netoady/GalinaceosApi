from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Avicula import Avicula

'''
  Manipulação do banco de dados para a entidade Avicula.
'''


class AviculaRepository():
    def getAll(self, filtros=None):
        stmt = select(Avicula)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getByIdAvicula(self, id):
        logger.info("Consultando avícula pelo id.")
        return db.session.get(Avicula, id)

    def insert(self, nome, cnpj, endereco):
        avicula = Avicula(nome, cnpj, endereco)
        db.session.add(avicula)
        db.session.commit()
        logger.info(f"Avícula inserida com id: {avicula.id}")
        return avicula

    def update(self, id, nome, cnpj, endereco):
        avicula = db.session.get(Avicula, id)
        if avicula is None:
            return None
        avicula.nome = nome
        avicula.cnpj = cnpj
        avicula.endereco = endereco
        db.session.commit()
        return avicula

    def delete(self, id):
        avicula = db.session.get(Avicula, id)
        if avicula is None:
            return False
        db.session.delete(avicula)
        db.session.commit()
        return True