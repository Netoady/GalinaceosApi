from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models.NomeTerritorio import NomeTerritorioSchema
from services.NomeTerritorioService import NomeTerritorioService
from helpers.logger import logger

nometerritorio_bp = Blueprint('nome territorio', __name__, url_prefix='/nometerritorio')


@nometerritorio_bp.get("/")
def getNomeTerritorio():
    logger.info("Listando todos os nomes territoriais")
    nometerritorio = NomeTerritorioService().getAll()
    return [a.toDict() for a in nometerritorio], 200


@nometerritorio_bp.get("/<int:id>")
def getById(id: int):
    logger.info(f"Listando nome territorial pelo id: {id}")
    nometerritorio = NomeTerritorioService().getById(id)
    if nometerritorio is None:
        return {"mensagem": "Nome Territorial não foi encontrada"}, 404
    return nometerritorio.toDict(), 200


@nometerritorio_bp.post("/")
def postNomeTerritorio():
    try:
        data = NomeTerritorioSchema().load(request.get_json())
        nometerritorio = NomeTerritorioService().create(data)
        return nometerritorio.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@nometerritorio_bp.put("/<int:id>")
def putNomeTerritorio(id: int):
    try:
        data = NomeTerritorioSchema().load(request.get_json())
        nometerritorio = NomeTerritorioService().update(id, data)
        if nometerritorio is None:
            return {"mensagem": "Nome Territorial não foi encontrado"}, 404
        return nometerritorio.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


@nometerritorio_bp.delete("/<int:id>")
def deleteNomeTerritorio(id: int):
    logger.info(f"Removendo nome territorial id: {id}")
    removido = NomeTerritorioService().delete(id)
    if not removido:
        return {"mensagem": "Nome territorial não foi encontrado"}, 404
    return {"mensagem": "Nome Territorial removido com sucesso!"}, 200