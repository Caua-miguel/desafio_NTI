from flask import Blueprint, jsonify
from project.services.branches_services import Branche
from project.controllers.api_controller import cnpjs

branches_blueprint = Blueprint("branche", __name__)

@branches_blueprint.route("/")
def list_branches():
    brs = Branche.select_branches()

    if not brs:
        return jsonify({"error": "No branches found!"}), 409
    
    return jsonify(brs), 201

@branches_blueprint.route("/filiais")
def insert_branches():

    branches_exists = Branche.branches_exists()
    if branches_exists:
        return jsonify({"error": "Branche already exists!"}), 409
    
    Branche.insert_branches(cnpjs)
    return jsonify({"message: ": "Branch added successfully! "}), 201

# delete não vai para a versão final
@branches_blueprint.route("/filiais/<string:cnpj>/delete", methods=["DELETE"])
def delete_branches(cnpj):
        Branche.delete_branches(cnpj)
        return jsonify({'message': 'Branch deleted successfully!'}), 201
