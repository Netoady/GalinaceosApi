from helpers.logger import logger
from repository.NivelTerritorialRepository import NivelTerritorialRepository
from models.NivelTerritorial import NivelTerritorial


def rowToNivelTerritorial(row):
    id = row[0]
    sigla = row[1]
    descricao = row[2]
    return NivelTerritorial(id, sigla, descricao)


class NivelTerritorialService():

    def __init__(self):
        self.nivelterritorialRepository = NivelTerritorialRepository()

    def getAll(self):
        rows = self.nivelterritorialRepository.getAll()
        logger.info(f"Retornando {len(rows)} nivel territorial")
        return [rowToNivelTerritorial(r) for r in rows]  

    def getById(self, id):
        row = self.nivelterritorialRepository.getById(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToNivelTerritorial(row) if row is not None else None

    def create(self, data):
        sigla = data["sigla"]
        descricao = data["descricao"]
        id = self.nivelterritorialRepository.insert(
            sigla, descricao
        )
        logger.info(f"Nivel Territorial criado com id: {id}")
        return NivelTerritorial(id,  sigla, descricao)  

    def update(self, id, data):
        affected = self.nivelterritorialRepository.update(
            id, data["sigla"], data["descricao"]
        )
        if affected == 0:
            return None
        logger.info(f"Nivel Territorial {id} atualizado")
        return NivelTerritorial(id, data["sigla"], data["descricao"])

    def delete(self, id):
        affected = self.nivelterritorialRepository.delete(id)
        logger.info(f"Nivel Territorial {id} removido: {affected > 0}")
        return affected > 0