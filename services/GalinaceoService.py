from helpers.logger import logger
from repository.GalinaceoRepository import GalinaceoRepository

class GalinaceoService:
    def __init__(self):
        self.galinaceoRepository = GalinaceoRepository()

    def getAll(self, filtros: dict = None):
        galinaceos = self.galinaceoRepository.getAll(filtros)
        logger.info(f"Retornando {len(galinaceos)} galináceos")
        return galinaceos

    def getByIdGalinaceo(self, id):
        galinaceo = self.galinaceoRepository.getByIdGalinaceo(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return galinaceo