from marshmallow import Schema, fields, validate
from flask_restful import fields as dto

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date

from helpers.database import db

# Campos para a formatação DTO no Restful.
avicultor_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'nascimento': dto.String,
    'cpf': dto.String,
    'caf': dto.String,
}


class Avicultor(db.Model):
    __tablename__ = "tb_avicultor"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(), nullable=False)
    nascimento: Mapped[Date] = mapped_column(Date(), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    caf: Mapped[str] = mapped_column(String(), nullable=False)

    enderecos: Mapped[list["Endereco"]] = relationship(back_populates="avicultor",cascade="all, delete-orphan")


class AvicultorSchema(Schema):
    nome = fields.Str(required=True, error_messages={
                      "required": "Adicione um nome."})
    nascimento = fields.Date(required=True)
    cpf = fields.Str(required=True, validate=validate.Length(
        max=11, error="Tamanho do CPF inválido."), error_messages={"required": "Adicione um CPF.", "invalid": "Valor inválido."})
    caf = fields.Str(required=True)