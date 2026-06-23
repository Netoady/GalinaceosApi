from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Nome Territorio.
'''


class NomeTerritorioRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Nome_Territorio")
        return cursor.fetchall()

    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        cursor.execute("SELECT * FROM Nome_Territorio WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, nome):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Nome_Territorio(nome) VALUES(%s)",
            (nome)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, nome):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Nome_Territorio SET nome=%s WHERE id=%s",
            (nome, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Nome_Territorio WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount