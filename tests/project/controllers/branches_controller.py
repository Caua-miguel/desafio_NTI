from project import app
from project.api import data_brances
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that insert data was correctly
    def test_insert_branches(self):
        tester = app.test_client(self)
        response = tester.get('/filiais', content_data='html/text')
        
        cnpjs = [
            '82110818000121','82110818000202',
        ]

        empyt_list = []

        list = data_brances()
        pass
