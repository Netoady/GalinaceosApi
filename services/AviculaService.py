from marshmallow import ValidationError
from helpers.logger import logger
from repository.AviculaRepository import AviculaRepository
from services.AvicultorService import AvicultorService

class AviculaService():
    def __init__(self):
        self.aviculaRepository = AviculaRepository()

    def _validarAvicultor(self, avicultor_id):
        avicultor = AvicultorService().getByIdAvicultor(avicultor_id)
        if avicultor is None:
            raise ValidationError({"avicultor_id": ["Avicultor não encontrado."]})

    def getAll(self, filtros: dict = None):
        aviculas = self.aviculaRepository.getAll(filtros)
        logger.info(f"Retornando {len(aviculas)} avículas")
        return aviculas

    def getByIdAvicula(self, id):
        avicula = self.aviculaRepository.getByIdAvicula(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return avicula

    def create(self, data):
        self._validarAvicultor(data["avicultor_id"])
        avicula = self.aviculaRepository.insert(
            data["nome"], str(data["cnpj"]), data["endereco"], data["avicultor_id"]
        )
        logger.info(f"Avícula criada com id: {avicula.id}")
        return avicula

    def update(self, id, data):
        self._validarAvicultor(data["avicultor_id"])
        avicula = self.aviculaRepository.update(
            id, data["nome"], str(data["cnpj"]), data["endereco"], data["avicultor_id"]
        )
        if avicula is None:
            return None
        logger.info(f"Avícula {id} atualizada")
        return avicula

    def delete(self, id):
        removido = self.aviculaRepository.delete(id)
        logger.info(f"Avícula {id} removida: {removido}")
        return removido