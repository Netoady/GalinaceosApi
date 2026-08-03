CREATE TABLE IF NOT EXISTS tb_avicultor(
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    caf VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_endereco(
    id SERIAL PRIMARY KEY,
    logradouro TEXT NOT NULL,
    numero TEXT NOT NULL,
    cep TEXT NOT NULL,
    avicultor_id INT NOT NULL,
    CONSTRAINT fk_endereco_avicultor FOREIGN KEY (avicultor_id) REFERENCES tb_avicultor(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tb_avicula(
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    cnpj TEXT NOT NULL UNIQUE,
    endereco TEXT,
    avicultor_id INT NOT NULL,
    CONSTRAINT fk_avicula_avicultor FOREIGN KEY (avicultor_id) REFERENCES tb_avicultor(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tb_galpao(
    id SERIAL PRIMARY KEY,
    identificador TEXT NOT NULL,
    area_m2 REAL,
    avicula_id INT NOT NULL,
    CONSTRAINT fk_galpao_avicula FOREIGN KEY (avicula_id) REFERENCES tb_avicula(id) ON DELETE CASCADE
);

CREATE TABLE tb_galinaceo (
    id SERIAL PRIMARY KEY,
    sist_cria VARCHAR(50),
    niv_terr VARCHAR(50),
    cod_terr VARCHAR(50),
    nom_terr VARCHAR(100),
    cl_gal VARCHAR(50),
    galpao_id INT NOT NULL,
    CONSTRAINT fk_galinaceo_galpao FOREIGN KEY (galpao_id) REFERENCES tb_galpao(id) ON DELETE CASCADE
);



