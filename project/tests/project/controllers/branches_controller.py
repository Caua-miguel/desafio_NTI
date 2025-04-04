from project import app
from database.config.db import db
from project.services.branches_services import Branche
import unittest

class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class FlaskTestCase(unittest.TestCase):

    print("TEST:")
    @classmethod
    def setUpClass(cls):
        print("TEST:")
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()        

    def test_insert_branches(self):
        print("TEST:")
        
        cnpjs = [
            '82110818000121','82110818000202',
        ]

        Branche.insert_branches(cnpjs)
        # print("TEST:" + response.data)
        # self.assertTrue(b'ALFA TRANSPORTES LTDA' in response.data)

if __name__ == '__main__':
    unittest.main()

