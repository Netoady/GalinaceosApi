from flask import Blueprint, request
from services.GalinaceoService import GalinaceoService
from helpers.logger import logger

galinaceos_bp = Blueprint('galinaceos', __name__, url_prefix='/galinaceos')

@galinaceos_bp.get("/")
def getGalinaceos():
    logger.info("Endpoint /galinaceos chamado com filtros opcionais")
    
    # Coleta os filtros passados na URL (?SIST_CRIA=...&NIV_TERR=...)
    filtros = {
        'SIST_CRIA': request.args.get('SIST_CRIA'),
        'NIV_TERR': request.args.get('NIV_TERR'),
        'COD_TERR': request.args.get('COD_TERR'),
        'NOM_TERR': request.args.get('NOM_TERR'),
        'CL_GAL': request.args.get('CL_GAL')
    }
    
    galinaceos = GalinaceoService().queryGalinaceos(filtros)
    return [g.toDict() for g in galinaceos], 200