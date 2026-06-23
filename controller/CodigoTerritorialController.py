from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models.CodigoTerritorial import CodigoTerritorialSchema
from services.CodigoTerritorialService import CodigoTerritorialService
from helpers.logger import logger

codigoterritorial_bp = Blueprint('codigo territorial', __name__, url_prefix='/codigoterritorial')


@codigoterritorial_bp.get("/")
def getCodigoTerritorial():
    logger.info("Listando todos os codigos territoriais")
    codigoterritorial = CodigoTerritorialService().getAll()
    return [a.toDict() for a in codigoterritorial], 200


@codigoterritorial_bp.get("/<int:id>")
def getById(id: int):
    logger.info(f"Listando codigo territorial pelo id: {id}")
    codigoterritorial = CodigoTerritorialService().getById(id)
    if codigoterritorial is None:
        return {"mensagem": "Codigo Territorial não foi encontrada"}, 404
    return codigoterritorial.toDict(), 200


@codigoterritorial_bp.post("/")
def postCodigoTerritorial():
    try:
        data = CodigoTerritorialSchema().load(request.get_json())
        codigoterritorial = CodigoTerritorialService().create(data)
        return codigoterritorial.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@codigoterritorial_bp.put("/<int:id>")
def putCodigoTerritorial(id: int):
    try:
        data = CodigoTerritorialSchema().load(request.get_json())
        codigoterritorial = CodigoTerritorialService().update(id, data)
        if codigoterritorial is None:
            return {"mensagem": "Codigo Territorial não foi encontrado"}, 404
        return codigoterritorial.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


@codigoterritorial_bp.delete("/<int:id>")
def deleteCodigoTerritorial(id: int):
    logger.info(f"Removendo codigo territorial id: {id}")
    removido = CodigoTerritorialService().delete(id)
    if not removido:
        return {"mensagem": "Codigo territorial não foi encontrado"}, 404
    return {"mensagem": "Codigo Territorial removido com sucesso!"}, 200