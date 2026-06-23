from helpers.database import get_conn
from helpers.logger import logger

class GalinaceoRepository:
    def getComFiltros(self, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal):
        conn = get_conn()
        cursor = conn.cursor()
        
        # Base da query baseada na tabela que o seed criou
        query = "SELECT id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal FROM galinaceos WHERE 1=1"
        params = []
        
        if sist_cria:
            query += " AND sist_cria = %s"
            params.append(sist_cria)
        if niv_terr:
            query += " AND niv_terr = %s"
            params.append(niv_terr)
        if cod_terr:
            query += " AND cod_terr = %s"
            params.append(int(cod_terr))
        if nom_terr:
            query += " AND nom_terr ILIKE %s"
            params.append(f"%{nom_terr}%")
        if cl_gal:
            query += " AND cl_gal = %s"
            params.append(int(cl_gal))
            
        logger.info(f"Executando busca dinâmica de galináceos. Query: {query}")
        cursor.execute(query, tuple(params))
        return cursor.fetchall()