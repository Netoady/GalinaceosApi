from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models.ClasseCbcaGal import ClasseCbcaGalSchema
from services.ClasseCbcaGalService import ClasseCbcaGalService
from helpers.logger import logger

classcbcagal_bp = Blueprint('classe cabeca gal', __name__, url_prefix='/classcbcagal')


@classcbcagal_bp.get("/")
def getClasseCbcaGal():
    logger.info("Listando todos as classes cabeça gal")
    classecbcagal = ClasseCbcaGalService().getAll()
    return [a.toDict() for a in classecbcagal], 200


@classcbcagal_bp.get("/<int:id>")
def getById(id: int):
    logger.info(f"Listando classe cabeca pelo id: {id}")
    classecbcagal = ClasseCbcaGalService().getById(id)
    if classecbcagal is None:
        return {"mensagem": "Classe Cabeca não foi encontrada"}, 404
    return classecbcagal.toDict(), 200


@classcbcagal_bp.post("/")
def postClasseCbcaGal():
    try:
        data = ClasseCbcaGalSchema().load(request.get_json())
        classecbcagal = ClasseCbcaGalService().create(data)
        return classecbcagal.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@classcbcagal_bp.put("/<int:id>")
def putClasseCbcaGal(id: int):
    try:
        data = ClasseCbcaGalSchema().load(request.get_json())
        classecbcagal = ClasseCbcaGalService().update(id, data)
        if classecbcagal is None:
            return {"mensagem": "Classe cabeca não foi encontrada"}, 404
        return classecbcagal.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


@classcbcagal_bp.delete("/<int:id>")
def deleteClasseCbcaGal(id: int):
    logger.info(f"Removendo avicultor id: {id}")
    removido = ClasseCbcaGalService().delete(id)
    if not removido:
        return {"mensagem": "Classe cabeca não foi encontrada"}, 404
    return {"mensagem": "Classe cabeca removida com sucesso!"}, 200