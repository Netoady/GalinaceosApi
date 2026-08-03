from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Galinaceo import Galinaceo

class GalinaceoRepository:
    def getAll(self, filtros: dict = None):
        stmt = select(Galinaceo)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getByIdGalinaceo(self, id):
        logger.info("Consultando galináceo pelo id.")
        return db.session.get(Galinaceo, id)