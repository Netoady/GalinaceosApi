from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Nível Territorial.
'''


class NivelTerritorialRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Nivel_Territorial")
        return cursor.fetchall()

    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        cursor.execute("SELECT * FROM Nivel_Territorial WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Nivel_Territorial(sigla, descricao) VALUES(%s, %s)",
            (sigla, descricao)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Nivel_Territorial SET sigla=%s, descricao=%s WHERE id=%s",
            (sigla, descricao, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Nivel_Territorial WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount