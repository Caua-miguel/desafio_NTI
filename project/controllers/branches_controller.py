from flask import Blueprint, jsonify, request
from project.services.branches_services import Branche
from database.models.branches import db, Branches

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
    
    Branche.insert_branches()
    return jsonify({"message: ": "Branch added successfully! "}), 201

@branches_blueprint.route("/filiais/<string:cnpj>/delete", methods=["GET", "DELETE"])
def delete_branches(cnpj):
    branche_by_cnpj = db.session.query(Branches).filter_by(tbb_s_cnpj=cnpj).first_or_404()

    if request.method == "DELETE":
        db.session.delete(branche_by_cnpj)
        db.session.commit()
        return jsonify({'message': 'Branch deleted successfully!'}), 201
    return jsonify({'message': 'Use the delete method'}), 201