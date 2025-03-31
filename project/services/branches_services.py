from database.config.db import db
from database.models.branches import Branches
from project.api import data_brances
import re

class Branche:

    def select_branches():
        branches = db.session.query(Branches).all()
        br_list = [br.as_dict() for br in branches]
        return br_list
    
    def branches_exists():
        branche_exists = Branches.query.first() is not None
        return branche_exists
    
    def insert_branches():
        data = data_brances()
        for branches in data:
            branches['cnpj'] = re.sub(r'\D','', branches['cnpj'])
            new_branches = Branches(tbb_s_cnpj=branches['cnpj'], tbb_s_name=branches["name"], tbb_s_city=branches["city"], tbb_s_state=branches["state"])
            db.session.add(new_branches)
            db.session.commit()
        return
    
    def delete_branches(cnpj):
        branche_by_cnpj = db.session.query(Branches).filter_by(tbb_s_cnpj=cnpj).first_or_404()
        db.session.delete(branche_by_cnpj)
        db.session.commit()
        return