from marshmallow import Schema, fields
from flask_restful import fields as dto

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

from helpers.database import db

galpao_fields = {
    'id': dto.Integer,
    'identificador': dto.String,
    'area_m2': dto.Integer,
    'avicula_id': dto.Integer,
}


class Galpao(db.Model):
    __tablename__ = "tb_galpao"

    id: Mapped[int] = mapped_column(primary_key=True)
    identificador: Mapped[str] = mapped_column(String(), nullable=False)
    area_m2: Mapped[int] = mapped_column(Integer(), nullable=False)
    avicula_id: Mapped[int] = mapped_column(ForeignKey("tb_avicula.id"), nullable=False)

    avicula: Mapped["Avicula"] = relationship("Avicula", back_populates="galpoes")
    galinaceos: Mapped[list["Galinaceo"]] = relationship("Galinaceo", back_populates="galpao", cascade="all, delete-orphan")


class GalpaoSchema(Schema):
    identificador = fields.Str(required=True, error_messages={
                    "required": "Adicione um identificador."
    })
    area_m2 = fields.Int(required=True, error_messages={"required": "Informe a area do galpao: "})
    avicula_id = fields.Int(required=True, error_messages={
                    "required": "Informe a avicula."})


