from helpers.logger import logger
from repository.CodigoTerritorialRepository import CodigoTerritorialRepository
from models.CodigoTerritorial import CodigoTerritorial


def rowToCodigoTerritorial(row):
    id = row[0]
    codigo = row[1]
    descricao = row[2]
    return CodigoTerritorial(id, codigo, descricao)


class CodigoTerritorialService():

    def __init__(self):
        self.codigoterritorialRepository = CodigoTerritorialRepository()

    def getAll(self):
        rows = self.codigoterritorialRepository.getAll()
        logger.info(f"Retornando {len(rows)} codigo territorial")
        return [rowToCodigoTerritorial(r) for r in rows]  

    def getById(self, id):
        row = self.codigoterritorialRepository.getById(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToCodigoTerritorial(row) if row is not None else None

    def create(self, data):
        codigo = data["codigo"]
        descricao = data["descricao"]
        id = self.codigoterritorialRepository.insert(
            codigo, descricao
        )
        logger.info(f"Codigo Territorial criado com id: {id}")
        return CodigoTerritorial(id,  codigo, descricao)  

    def update(self, id, data):
        affected = self.codigoterritorialRepository.update(
            id, data["codigo"], data["descricao"]
        )
        if affected == 0:
            return None
        logger.info(f"Codigo Territorial {id} atualizado")
        return CodigoTerritorial(id, data["codigo"], data["descricao"])

    def delete(self, id):
        affected = self.codigoterritorialRepository.delete(id)
        logger.info(f"Codigo Territorial {id} removido: {affected > 0}")
        return affected > 0