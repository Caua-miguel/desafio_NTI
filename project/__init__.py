from flask import Flask, request, jsonify
from database.models.branches import db, Branches
from database.config.conn import AplicationConfig
from flask_migrate import Migrate
from project.api import data_brances
import re

app = Flask(__name__)

app.config.from_object(AplicationConfig)
db.init_app(app)

migrate = Migrate(app, db)

@app.route("/filiais")
def insert_branches():
    
    data = data_brances()
    city = data[0]["city"]
    print(f"Cidade da lista: {city}")
    branches_exists = Branches.query.filter_by(tbb_s_city=city).first() is not None

    if branches_exists:
        return jsonify({"error": "Branche already exists!"}), 409
    
    for branches in data:
        branches['cnpj'] = re.sub(r'\D','', branches['cnpj'])
        new_branches = Branches(tbb_s_cnpj=branches['cnpj'], tbb_s_name=branches["name"], tbb_s_city=branches["city"], tbb_s_state=branches["state"])
        db.session.add(new_branches)
        db.session.commit()
    return jsonify({"message: ": "Branch added successfully! "}), 201

@app.route("/teste")
def teste():
    return jsonify({"teste": "teste"})

@app.route("/filiais/<string:cnpj>/delete", methods=["GET", "DELETE"])
def delete_branches(cnpj):
    branche_by_cnpj = db.session.query(Branches).filter_by(tbb_s_cnpj=cnpj).first_or_404()

    if request.method == "DELETE":
        db.session.delete(branche_by_cnpj)
        db.session.commit()
        return jsonify({'message': 'Branch deleted successfully!'}), 201
    return jsonify({'message': 'Use the delete method'}), 201

