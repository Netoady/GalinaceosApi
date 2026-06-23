from helpers.logger import logger
from repository.ClasseCbcaGalRepository import ClasseCbcaGalRepository
from models.ClasseCbcaGal import ClasseCbcaGal


def rowToClasseCbcaGal(row):
    id = row[0]
    codigo = row[1]
    descricao = row[2]
    return ClasseCbcaGal(id, codigo, descricao)


class ClasseCbcaGalService():

    def __init__(self):
        self.classecbcagalRepository = ClasseCbcaGalRepository()

    def getAll(self):
        rows = self.classecbcagalRepository.getAll()
        logger.info(f"Retornando {len(rows)} classecbcagal")
        return [rowToClasseCbcaGal(r) for r in rows]  

    def getById(self, id):
        row = self.classecbcagalRepository.getById(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToClasseCbcaGal(row) if row is not None else None

    def create(self, data):
        codigo = data["codigo"]
        descricao = data["descricao"]
        id = self.classecbcagalRepository.insert(
            codigo, descricao
        )
        logger.info(f"Classe Cabeca criado com id: {id}")
        return ClasseCbcaGal(id,  codigo, descricao)  

    def update(self, id, data):
        affected = self.classecbcagalRepository.update(
            id, data["codigo"], data["descricao"]
        )
        if affected == 0:
            return None
        logger.info(f"Classe Cabeça {id} atualizada")
        return ClasseCbcaGal(id, data["codigo"], data["descricao"])

    def delete(self, id):
        affected = self.classecbcagalRepository.delete(id)
        logger.info(f"Classe Cabeca {id} removida: {affected > 0}")
        return affected > 0