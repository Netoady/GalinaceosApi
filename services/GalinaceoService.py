from helpers.logger import logger
from repository.GalinaceoRepository import GalinaceoRepository
from models.Galinaceo import Galinaceo

def rowToGalinaceo(row):
    return Galinaceo(
        id=row[0],
        sist_cria=row[1],
        niv_terr=row[2],
        cod_terr=row[3],
        nom_terr=row[4],
        cl_gal=row[5],
        nom_cl_gal=row[6]
    )

class GalinaceoService:
    def __init__(self):
        self.galinaceoRepository = GalinaceoRepository()

    def queryGalinaceos(self, filtros):
        rows = self.galinaceoRepository.getComFiltros(
            sist_cria=filtros.get('SIST_CRIA'),
            niv_terr=filtros.get('NIV_TERR'),
            cod_terr=filtros.get('COD_TERR'),
            nom_terr=filtros.get('NOM_TERR'),
            cl_gal=filtros.get('CL_GAL')
        )
        logger.info(f"Retornando {len(rows)} registros filtrados de galináceos")
        return [rowToGalinaceo(r) for r in rows]