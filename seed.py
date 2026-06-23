import pandas as pd
import numpy as np
from helpers.application import app
from helpers.database import get_conn

def criar_tabela_e_carregar_dados():
    print("1. Lendo e tratando o arquivo GALINACEOS.csv com Pandas...")
    
    # Lemos o CSV mapeando o separador ';' e tratando valores nulos ou vazios
    df = pd.read_csv('GALINACEOS.csv', sep=';', na_values=['X', ' ', ''])
    
    # Tratamento inicial com Pandas/NumPy para evitar quebra de tipos no banco
    df['COD_TERR'] = df['COD_TERR'].fillna(0).astype(int)
    df['CL_GAL'] = df['CL_GAL'].fillna(0).astype(int)
    
    # Usamos o contexto do app do Flask para que o get_conn() funcione perfeitamente
    with app.app_context():
        conn = get_conn()
        cursor = conn.cursor()
        
        print("2. Criando a tabela 'galinaceos' caso ela não exista...")
        # Criamos a tabela com as 5 colunas principais de filtros + colunas auxiliares
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS galinaceos (
                id SERIAL PRIMARY KEY,
                sist_cria VARCHAR(100),
                niv_terr VARCHAR(50),
                cod_terr INTEGER,
                nom_terr VARCHAR(150),
                cl_gal INTEGER,
                nom_cl_gal VARCHAR(150)
            );
        """)
        conn.commit()
        
        print("3. Inserindo os dados do DataFrame no PostgreSQL...")
        query_insert = """
            INSERT INTO galinaceos (sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        
        # O iterrows() do Pandas percorre linha por linha de forma eficiente
        for index, row in df.iterrows():
            valores = (
                str(row['SIST_CRIA']) if pd.notna(row['SIST_CRIA']) else None,
                str(row['NIV_TERR']) if pd.notna(row['NIV_TERR']) else None,
                int(row['COD_TERR']),
                str(row['NOM_TERR']) if pd.notna(row['NOM_TERR']) else None,
                int(row['CL_GAL']),
                str(row['NOM_CL_GAL']) if pd.notna(row['NOM_CL_GAL']) else None
            )
            cursor.execute(query_insert, valores)
            
        # Confirma todas as operações de uma vez só no banco
        conn.commit()
        cursor.close()
        print(f"Sucesso total! {len(df)} registros foram extraídos e salvos no banco.")

if __name__ == "__main__":
    criar_tabela_e_carregar_dados()