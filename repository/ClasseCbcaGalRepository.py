from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Classe Cabeça Galinaceos.
'''


class ClasseCbcaGalRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Classe_Cbca_Gal")
        return cursor.fetchall()

    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        cursor.execute("SELECT * FROM Classe_Cbca_Gal WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Classe_Cbca_Gal(codigo, descricao) VALUES(%s, %s)",
            (codigo, descricao)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Classe_Cbca_Gal SET codigo=%s, descricao=%s WHERE id=%s",
            (codigo, descricao, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Classe_Cbca_Gal WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount