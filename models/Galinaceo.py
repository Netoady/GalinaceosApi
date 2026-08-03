from marshmallow import Schema, fields
from flask_restful import fields as dto

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

from helpers.database import db

galinaceo_fields = {
    'id': dto.Integer,
    'sist_cria': dto.String,
    'niv_terr': dto.String,
    'cod_terr': dto.String,
    'nom_terr': dto.String,
    'cl_gal': dto.String,
    'galpao_id': dto.Integer,
}

class Galinaceo(db.Model):
    __tablename__ = "tb_galinaceo"

    id: Mapped[int] = mapped_column(primary_key=True)
    sist_cria: Mapped[str] = mapped_column(String(), nullable=False)
    niv_terr: Mapped[str] = mapped_column(String(), nullable=False)
    cod_terr: Mapped[str] = mapped_column(String(), nullable=False)
    nom_terr: Mapped[str] = mapped_column(String(), nullable=False)
    cl_gal: Mapped[str] = mapped_column(String(), nullable=False)

    galpao_id: Mapped[int] = mapped_column(ForeignKey("tb_galpao.id"), nullable=False)

    galpao: Mapped["Galpao"] = relationship("Galpao", back_populates="galinaceos")


class GalinaceoSchema(Schema):
    sist_cria = fields.Str(required=True, error_messages={
                      "required": "Adicione um sistema de criação."})
    niv_terr = fields.Str(required=True, error_messages={
                      "required": "Adicione um nível de terreno."})
    cod_terr = fields.Str(required=True, error_messages={
                      "required": "Adicione um código de terreno."})
    nom_terr = fields.Str(required=True, error_messages={
                      "required": "Adicione um nome de terreno."})
    cl_gal = fields.Str(required=True, error_messages={
                      "required": "Adicione uma classe de galináceo."})
    galpao_id = fields.Int(required=True, error_messages={
                               "required": "Informe o galpão."})