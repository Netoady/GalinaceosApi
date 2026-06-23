CREATE TABLE IF NOT EXISTS Sistema_Criacao {
  id serial primary key,
  sigla varchar not null,
  descricao varchar not null
};

CREATE TABLE IF NOT EXISTS Nivel_Territorial {
  id serial primary key,
  sigla varchar not null,
  descricao varchar not null
};

CREATE TABLE IF NOT EXISTS Codigo_Territorial {
  id serial primary key,
  codigo text not null,
  descricao varchar
};

CREATE TABLE IF NOT EXISTS Nome_Territorio {
  id serial primary key,
  nome varchar not null,
};

CREATE TABLE IF NOT EXISTS Classe_Cbca_Gal {
  id serial primary key,
  codigo int not null,
  descricao varchar not null
};