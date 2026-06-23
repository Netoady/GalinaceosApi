from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Sistema Criacao.
'''


class SistemaCriacaoRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sistema_Criacao")
        return cursor.fetchall()

    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        cursor.execute("SELECT * FROM Sistema_Criacao WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Sistema_Criacao(sigla, descricao) VALUES(%s, %s)",
            (sigla, descricao)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Sistema_Criacao SET sigla=%s, descricao=%s WHERE id=%s",
            (sigla, descricao, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Sistema_Criacao WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount