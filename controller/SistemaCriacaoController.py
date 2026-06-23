from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models.SistemaCriacao import SistemaCriacaoSchema
from services.SistemaCriacaoService import SistemaCriacaoService
from helpers.logger import logger

sistemacriacao_bp = Blueprint('sistema criacao', __name__, url_prefix='/sistemacriacao')


@sistemacriacao_bp.get("/")
def getSistemaCriacao():
    logger.info("Listando todos os sistemas de criacao")
    sistemacriacao = SistemaCriacaoService().getAll()
    return [a.toDict() for a in sistemacriacao], 200


@sistemacriacao_bp.get("/<int:id>")
def getById(id: int):
    logger.info(f"Listando sistema de criacao pelo id: {id}")
    sistemacriacao = SistemaCriacaoService().getById(id)
    if sistemacriacao is None:
        return {"mensagem": "Sistema Criacao não foi encontrado"}, 404
    return sistemacriacao.toDict(), 200


@sistemacriacao_bp.post("/")
def postSistemaCriacao():
    try:
        data = SistemaCriacaoSchema().load(request.get_json())
        sistemacriacao = SistemaCriacaoService().create(data)
        return sistemacriacao.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@sistemacriacao_bp.put("/<int:id>")
def putSistemaCriacao(id: int):
    try:
        data = SistemaCriacaoSchema().load(request.get_json())
        sistemacriacao = SistemaCriacaoService().update(id, data)
        if sistemacriacao is None:
            return {"mensagem": "Sistema Criacao não foi encontrado"}, 404
        return sistemacriacao.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


@sistemacriacao_bp.delete("/<int:id>")
def deleteSistemaCriacao(id: int):
    logger.info(f"Removendo nome territorial id: {id}")
    removido = SistemaCriacaoService().delete(id)
    if not removido:
        return {"mensagem": "Sistema Criacao não foi encontrada"}, 404
    return {"mensagem": "Sistema Criacao removido com sucesso!"}, 200