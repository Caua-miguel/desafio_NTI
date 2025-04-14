from database.config.db import db
from database.models.branches import Branches
from project.services.api_services import BranchesAlfa
from logging import info, debug
import re

class Branche:

    def select_branches():
        branches = db.session.query(Branches).all()
        br_list = [br.as_dict() for br in branches]
        debug(f"Def select_branches returned list: {br_list}")
        info("The list was returned successfully")
        return br_list
    
    def branches_exists():
        branche_exists = Branches.query.first() is not None
        debug(f"Def branches_exists returned list: {branche_exists}")
        return branche_exists
    
    def insert_branches(cnpjs):
        brs_alfa = BranchesAlfa(cnpjs)
        data = brs_alfa.collect_branches_data()
        debug(f"Def insert_branches returned list: {data}")
        for branches in data:
            branches['cnpj'] = re.sub(r'\D','', branches['cnpj'])
            new_branches = Branches(tbb_s_cnpj=branches['cnpj'], tbb_s_name=branches["name"], tbb_s_city=branches["city"], tbb_s_state=branches["state"])
            db.session.add(new_branches)
            db.session.commit()
            info("Branch successfully extended")
        return {}
    
    def delete_branches(cnpj):
        branche_by_cnpj = db.session.query(Branches).filter_by(tbb_s_cnpj=cnpj).first_or_404()
        db.session.delete(branche_by_cnpj)
        db.session.commit()
        return {}