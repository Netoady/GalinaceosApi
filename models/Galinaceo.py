class Galinaceo:
    def __init__(self, id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal):
        self.id = id
        self.sist_cria = sist_cria
        self.niv_terr = niv_terr
        self.cod_terr = cod_terr
        self.nom_terr = nom_terr
        self.cl_gal = cl_gal
        self.nom_cl_gal = nom_cl_gal

    def toDict(self):
        return {
            "id": self.id,
            "SIST_CRIA": self.sist_cria,
            "NIV_TERR": self.niv_terr,
            "COD_TERR": self.cod_terr,
            "NOM_TERR": self.nom_terr,
            "CL_GAL": self.cl_gal,
            "NOM_CL_GAL": self.nom_cl_gal
        }