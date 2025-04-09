# from database.models.branches import  Branches
# from database.config.db import db

# def test_insert_in_branches_table():
#     new_branche = Branches(tbb_s_cnpj='82110818000121', tbb_s_name='ALFA TRANSPORTES LTDA', tbb_s_city="CACADOR", tbb_s_state="SC")
#     db.session.add(new_branche)
#     db.session.commit()

#     branche_exists = Branches.query.first()
#     assert branche_exists is not None