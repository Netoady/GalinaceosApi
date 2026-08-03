from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Galpao import Galpao

'''
  Manipulação do banco de dados para a entidade Galpao.
'''


class GalpaoRepository():
    def getAll(self, filtros=None):
        stmt = select(Galpao)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getByIdGalpao(self, id):
        logger.info("Consultando galpão pelo id.")
        return db.session.get(Galpao, id)

    def insert(self, identificador, area_m2, avicula_id):
        galpao = Galpao(identificador, area_m2, avicula_id)
        db.session.add(galpao)
        db.session.commit()
        logger.info(f"Galpão inserido com id: {galpao.id}")
        return galpao

    def update(self, id, identificador, area_m2):
        galpao = db.session.get(Galpao, id)
        if galpao is None:
            return None
        galpao.identificador = identificador
        galpao.area_m2 = area_m2
        galpao.avicula_id = avicula_id
        db.session.commit()
        return galpao

    def delete(self, id):
        galpao = db.session.get(Galpao, id)
        if galpao is None:
            return False
        db.session.delete(galpao)
        db.session.commit()
        return True