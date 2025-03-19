from database.config.db import db
from uuid import uuid4

def get_uuid():
    return uuid4().hex

class Branches(db.Model):
    __tablename__ = 'branches'

    tbb_i_code = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    tbb_s_cnpj = db.Column(db.String(14), nullable=False)
    tbb_s_name = db.Column(db.String(255), nullable=False)
    tbb_s_city = db.Column(db.String(255), nullable=False)
    tbb_s_state = db.Column(db.String(2), nullable=False)
 