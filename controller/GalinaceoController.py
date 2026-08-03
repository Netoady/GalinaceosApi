from flask import request
from flask_restful import Resource, marshal

from models.Galinaceo import galinaceo_fields
from services.GalinaceoService import GalinaceoService
from helpers.logger import logger

CAMPOS_FILTRO = {"SIST_CRIA", "NIV_TERR", "COD_TERR", "NOM_TERR", "CL_GAL"}

class GalinaceosController(Resource):
    def get(self):
        logger.info("Listando todos os galináceos")
        filtros = {key: value for key, value in request.args.items() if key in CAMPOS_FILTRO and value}
        galinaceos = GalinaceoService().getAll(filtros)
        return marshal(galinaceos, galinaceo_fields), 200