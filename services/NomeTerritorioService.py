from helpers.logger import logger
from repository.NomeTerritorioRepository import NomeTerritorioRepository
from models.NomeTerritorio import NomeTerritorio


def rowToNomeTerritorio(row):
    id = row[0]
    nome = row[1]
    return NomeTerritorio(id, nome)


class NomeTerritorioService():

    def __init__(self):
        self.nometerritorioRepository = NomeTerritorioRepository()

    def getAll(self):
        rows = self.nometerritorioRepository.getAll()
        logger.info(f"Retornando {len(rows)} nome do territorio")
        return [rowToNomeTerritorio(r) for r in rows]  

    def getById(self, id):
        row = self.nometerritorioRepository.getById(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToNomeTerritorio(row) if row is not None else None

    def create(self, data):
        nome = data["nome"]
        id = self.nometerritorioRepository.insert(
            nome
        )
        logger.info(f"Nome Territorio criado com id: {id}")
        return NomeTerritorio(id,  nome)

    def update(self, id, data):
        affected = self.nometerritorioRepository.update(
            id, data["nome"]
        )
        if affected == 0:
            return None
        logger.info(f"Nome Territorio {id} atualizado")
        return NomeTerritorio(id, data["nome"])

    def delete(self, id):
        affected = self.nometerritorioRepository.delete(id)
        logger.info(f"Nome Territorio {id} removido: {affected > 0}")
        return affected > 0