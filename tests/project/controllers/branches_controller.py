from project import app
from database.config.db import db
from project.services.branches_services import Branche
import unittest

class FlaskTestCase(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("Setting up the test environment...")
    #     with app.app_context():
    #         db.create_all()

    # @classmethod
    # def tearDownClass(cls):
    #     print("Tearing down the test environment...")
    #     with app.app_context():
    #         db.session.remove()
    #         db.drop_all()        

    # def test_insert_branches(self):
    #     print("Running test_insert_branches...")
        
    #     cnpjs = [
    #         '82110818000121','82110818000202',
    #     ]

    #     # Chama o método para inserir os CNPJs
    #     Branche.insert_branches(cnpjs)

    #     # Chama o método para selecionar os CNPJs
    #     select = Branche.select_branches()

    #     # Imprime o resultado da seleção
    #     print(select)
        
    #     # Aqui, podemos adicionar uma asserção para garantir que o método funcione corretamente
    #     self.assertEqual(len(select), len(cnpjs), "O número de registros selecionados não é igual ao número de CNPJs inseridos.")

    def test_example(self):
        print("Este é um teste simples!")
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
