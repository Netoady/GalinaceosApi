from marshmallow import Schema, fields, validate
from flask_restful import fields as dto

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from helpers.database import db

avicula_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'cnpj': dto.String,
    'endereco': dto.String,
}


class Avicula(db.Model):
    __tablename__ = "tb_avicula"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(14), nullable=False)
    endereco: Mapped[str] = mapped_column(String(), nullable=False)

    avicultor_id: Mapped[int] = mapped_column(ForeignKey("tb_avicultor.id"), nullable=False)

    avicultor: Mapped["Avicultor"] = relationship("Avicultor")
    galpoes: Mapped[list["Galpao"]] = relationship("Galpao", back_populates="avicula", cascade="all, delete-orphan")


class AviculaSchema(Schema):
    nome = fields.Str(required=True, error_messages={
                      "required": "Adicione um nome."})
    cnpj = fields.Str(required=True, validate=validate.Length(
        max=14, error="Tamanho do CNPJ inválido."), error_messages={"required": "Adicione um CNPJ.", "invalid": "Valor inválido."})
    endereco = fields.Str(required=True, error_messages={
                          "required": "Adicione um endereço."})
    avicultor_id = fields.Int(required=True, error_messages={
                               "required": "Informe o avicultor."})