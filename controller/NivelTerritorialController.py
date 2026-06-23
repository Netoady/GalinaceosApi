from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models.NivelTerritorial import NivelTerritorialSchema
from services.NivelTerritorialService import NivelTerritorialService
from helpers.logger import logger

nivelterritorial_bp = Blueprint('nivel territorial', __name__, url_prefix='/nivelterritorial')


@nivelterritorial_bp.get("/")
def getNivelTerritorial():
    logger.info("Listando todos os niveis territoriais")
    nivelterritorial = NivelTerritorialService().getAll()
    return [a.toDict() for a in nivelterritorial], 200


@nivelterritorial_bp.get("/<int:id>")
def getById(id: int):
    logger.info(f"Listando nivel territorial pelo id: {id}")
    nivelterritorial = NivelTerritorialService().getById(id)
    if nivelterritorial is None:
        return {"mensagem": "Nivel Territorial não foi encontrada"}, 404
    return nivelterritorial.toDict(), 200


@nivelterritorial_bp.post("/")
def postNivelTerritorial():
    try:
        data = NivelTerritorialSchema().load(request.get_json())
        nivelterritorial = NivelTerritorialService().create(data)
        return nivelterritorial.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@nivelterritorial_bp.put("/<int:id>")
def putNivelTerritorial(id: int):
    try:
        data = NivelTerritorialSchema().load(request.get_json())
        nivelterritorial = NivelTerritorialService().update(id, data)
        if nivelterritorial is None:
            return {"mensagem": "Nivel Territorial não foi encontrado"}, 404
        return nivelterritorial.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


@nivelterritorial_bp.delete("/<int:id>")
def deleteNivelTerritorial(id: int):
    logger.info(f"Removendo nivel territorial id: {id}")
    removido = NivelTerritorialService().delete(id)
    if not removido:
        return {"mensagem": "Nivel territorial não foi encontrado"}, 404
    return {"mensagem": "Nivel Territorial removido com sucesso!"}, 200