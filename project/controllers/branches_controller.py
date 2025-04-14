from flask import Blueprint, jsonify
from project.services.branches_services import Branche
from project.controllers.api_controller import cnpjs
from logging import info

branches_blueprint = Blueprint("branche", __name__)

@branches_blueprint.route("/")
def list_branches():
    info("Route call has been initiated")
    brs = Branche.select_branches()

    if not brs:
        info("The branches table is empty")
        return jsonify({"error": "No branches found!"}), 409
    info("The route was called successfully")
    return jsonify(brs), 201

@branches_blueprint.route("/filiais")
def insert_branches():
    info("Route call has been initiated")
    branches_exists = Branche.branches_exists()
    if branches_exists:
        return jsonify({"message": "Branche already exists!"}), 409
    
    Branche.insert_branches(cnpjs)
    info("The route was called successfully")
    return jsonify({"message: ": "Branch added successfully! "}), 201

# delete não vai para a versão final
@branches_blueprint.route("/filiais/<string:cnpj>/delete", methods=["DELETE"])
def delete_branches(cnpj):
        Branche.delete_branches(cnpj)
        return jsonify({'message': 'Branch deleted successfully!'}), 201
