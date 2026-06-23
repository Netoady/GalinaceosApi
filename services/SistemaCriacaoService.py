from helpers.logger import logger
from repository.SistemaCriacaoRepository import SistemaCriacaoRepository
from models.SistemaCriacao import SistemaCriacao


def rowToSistemaCriacao(row):
    id = row[0]
    sigla = row[1]
    descricao = row[2]
    return SistemaCriacao(id, sigla, descricao)


class SistemaCriacaoService():

    def __init__(self):
        self.sistemacriacaoRepository = SistemaCriacaoRepository()

    def getAll(self):
        rows = self.sistemacriacaoRepository.getAll()
        logger.info(f"Retornando {len(rows)} sistema de criacao")
        return [rowToSistemaCriacao(r) for r in rows]  

    def getById(self, id):
        row = self.sistemacriacaoRepository.getById(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToSistemaCriacao(row) if row is not None else None

    def create(self, data):
        sigla = data["sigla"]
        descricao = data["descricao"]
        id = self.sistemacriacaoRepository.insert(
            sigla, descricao
        )
        logger.info(f"Sistema de Criacao criado com id: {id}")
        return SistemaCriacao(id,  sigla, descricao)  

    def update(self, id, data):
        affected = self.sistemacriacaoRepository.update(
            id, data["sigla"], data["descricao"]
        )
        if affected == 0:
            return None
        logger.info(f"Sistema de Criacao {id} atualizado")
        return SistemaCriacao(id, data["sigla"], data["descricao"])

    def delete(self, id):
        affected = self.sistemacriacaoRepository.delete(id)
        logger.info(f"Sistema de Criacao {id} removido: {affected > 0}")
        return affected > 0